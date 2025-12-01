#!/usr/bin/env python3
"""
GitHub Actions версия скрипта для автоматического обновления IP-списков провайдеров.
Работает только в режиме "все провайдеры сразу".
"""
import json
import requests
import sys
import os
import subprocess
import time
from pathlib import Path

OUTPUT_DIR = "ip-lists"
ALL_IN_ONE_DIR = "ALL-IN-ONE"
PROVIDERS_CONFIG = "providers.json"
# Попробуем найти sing-box в разных местах
SINGBOX_PATHS = [
    "sing-box",                    # В PATH
    "/usr/local/bin/sing-box",     # Linux стандартное расположение
    "./sing-box",                  # Текущая директория
]

def load_providers_config(config_path):
    """Загрузка конфигурации провайдеров из JSON файла."""
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ОШИБКА: Файл конфигурации '{config_path}' не найден", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ОШИБКА: Ошибка чтения JSON: {e}", file=sys.stderr)
        sys.exit(1)

def fetch_asn_data_fallback(asn, api_key):
    """Резервный метод получения данных по ASN через ipapi.is API.
    
    Args:
        asn: ASN номер (с или без префикса AS)
        api_key: API ключ для ipapi.is
        
    Returns:
        dict: Данные в формате совместимом с основным API или None при ошибке
    """
    if not asn.startswith("AS"):
        asn = f"AS{asn}"
    
    if not api_key:
        print("  [!] API ключ для ipapi.is не найден", file=sys.stderr)
        return None
    
    url = f"https://api.ipapi.is?q={asn}&key={api_key}"
    
    try:
        print(f"  [*] Использую резервный API (ipapi.is)...")
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        
        # Конвертируем формат ipapi.is в формат основного API
        converted_data = {
            'prefixes': [],
            'prefixes6': []
        }
        
        # Обрабатываем IPv4 префиксы
        for prefix in data.get('prefixes', []):
            converted_data['prefixes'].append({'netblock': prefix})
        
        # Обрабатываем IPv6 префиксы
        for prefix6 in data.get('prefixesIPv6', []):
            converted_data['prefixes6'].append({'netblock': prefix6})
        
        total_prefixes = len(converted_data['prefixes']) + len(converted_data['prefixes6'])
        print(f"  [OK] Получено {total_prefixes} префиксов через резервный API")
        
        return converted_data
        
    except requests.RequestException as e:
        print(f"  [!] Резервный API также не удался: {e}", file=sys.stderr)
        return None

def fetch_asn_data_from_url(asn, url, max_retries=2, custom_headers=None):
    """Получение данных по ASN с конкретного URL с повторными попытками.
    
    Args:
        asn: ASN номер (с префиксом AS)
        url: URL для запроса
        max_retries: Максимальное количество попыток
        custom_headers: Дополнительные заголовки для запроса (опционально)
        
    Returns:
        dict: Данные ASN или None при ошибке
    """
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
    }
    
    # Применяем custom headers если переданы
    if custom_headers:
        headers.update(custom_headers)
    
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.get(url, headers=headers, timeout=15)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            if attempt < max_retries:
                wait_time = attempt * 5  # 5, 10, 15 секунд
                print(f"  [!] Попытка {attempt}/{max_retries} не удалась: {e}")
                print(f"  ⏳ Повтор через {wait_time} секунд...")
                time.sleep(wait_time)
            else:
                print(f"  [!] Не удалось после {max_retries} попыток: {e}", file=sys.stderr)
                return None
    
    return None

def fetch_asn_data(asn, max_retries=2):
    """Получение данных по ASN с API с каскадными резервными источниками.
    
    Порядок попыток:
    1. https://ipinfo.robinbraemer.workers.dev (2 попытки)
    2. https://falling-shape-b6eb.kotanoff-adm.workers.dev (2 попытки)
    3. https://ipinfo.io/widget/demo (2 попытки)
    4. https://api.ipapi.is с API ключом (1 попытка)
    """
    if not asn.startswith("AS"):
        asn = f"AS{asn}"
    
    # Основной источник
    print(f"  [*] Попытка получить данные с основного API...")
    url_primary = f"https://ipinfo.robinbraemer.workers.dev/{asn}"
    data = fetch_asn_data_from_url(asn, url_primary, max_retries)
    if data:
        return data
    
    # Резервный источник #1 (тот же формат)
    print(f"  [*] Переключаюсь на резервный API #1...")
    url_secondary = f"https://falling-shape-b6eb.kotanoff-adm.workers.dev/{asn}"
    data = fetch_asn_data_from_url(asn, url_secondary, max_retries)
    if data:
        return data
    
    # Резервный источник #2 (тот же формат, требует специальные headers)
    print(f"  [*] Переключаюсь на резервный API #2...")
    url_tertiary = f"https://ipinfo.io/widget/demo/{asn}"
    ipinfo_headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'content-type': 'application/json',
        'referer': 'https://ipinfo.io/'
    }
    data = fetch_asn_data_from_url(asn, url_tertiary, max_retries, custom_headers=ipinfo_headers)
    if data:
        return data
    
    # Резервный источник #3 (ipapi.is - другой формат)
    print(f"  [*] Переключаюсь на резервный API #3 (ipapi.is)...")
    api_key = os.environ.get('IPAPI_KEY')
    if api_key:
        return fetch_asn_data_fallback(asn, api_key)
    else:
        print(f"  [!] Резервный API #3 недоступен (IPAPI_KEY не установлен)", file=sys.stderr)
        return None

def process_provider(provider_name, asn_list):
    """Обработка всех ASN для одного провайдера.
    
    Args:
        provider_name: Название провайдера
        asn_list: Список ASN для обработки
        
    Returns:
        Tuple[str, list]: Кортеж из пути к JSON файлу и списка уникальных CIDR.
                          Возвращает (None, []) если CIDR не найдены.
    """
    print(f"\n[*] Обработка провайдера: {provider_name}")
    print(f"    ASN: {', '.join(asn_list)}")
    
    all_ip_cidrs = []
    
    for idx, asn in enumerate(asn_list):
        print(f"  [*] Загружаю {asn}...")
        
        # Задержка между запросами для избежания rate limiting
        if idx > 0:
            time.sleep(2)
        
        raw_data = fetch_asn_data(asn)
        
        if not raw_data:
            print(f"  [!] Не удалось загрузить {asn}, пропускаю", file=sys.stderr)
            continue
        
        for prefix in raw_data.get('prefixes', []):
            netblock = prefix.get('netblock', '').strip()
            if netblock:
                all_ip_cidrs.append(netblock)
        
        for prefix6 in raw_data.get('prefixes6', []):
            netblock = prefix6.get('netblock', '').strip()
            if netblock:
                all_ip_cidrs.append(netblock)
    
    unique_cidrs = sorted(set(all_ip_cidrs))
    
    if not unique_cidrs:
        print(f"[!] ВНИМАНИЕ: Не найдено IP CIDR для {provider_name}", file=sys.stderr)
        return None, []
    
    clash_data = {
        "version": 3,
        "rules": [
            {
                "ip_cidr": unique_cidrs
            }
        ]
    }
    
    folder_name = provider_name.lower()
    folder_path = os.path.join(OUTPUT_DIR, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    filename = f"{provider_name.lower()}.json"
    filepath = os.path.join(folder_path, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(clash_data, f, indent=2, ensure_ascii=False)
    
    print(f"  [OK] Создан: {filepath}")
    print(f"      Всего IP CIDR: {len(unique_cidrs)}")
    
    return filepath, unique_cidrs

def find_singbox_binary():
    """Поиск sing-box бинарника в системе."""
    for path in SINGBOX_PATHS:
        # Проверяем существование файла
        if os.path.exists(path) and os.access(path, os.X_OK):
            return path
        
        # Проверяем через which (для PATH)
        try:
            result = subprocess.run(
                ["which", path],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                found_path = result.stdout.strip()
                if found_path:
                    return found_path
        except:
            continue
    
    return None

def convert_json_to_srs(json_path, singbox_binary):
    """Конвертация JSON в SRS формат через sing-box."""
    if not os.path.exists(json_path):
        print(f"[!] Файл не найден: {json_path}", file=sys.stderr)
        return None
    
    srs_path = json_path.replace('.json', '.srs')
    
    try:
        cmd = [singbox_binary, "rule-set", "compile", "--output", srs_path, json_path]
        print(f"  [*] Конвертирую: {os.path.basename(json_path)} → {os.path.basename(srs_path)}")
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print(f"  [OK] Создан: {srs_path}")
            return srs_path
        else:
            print(f"  [!] ОШИБКА при конвертации: {result.stderr}", file=sys.stderr)
            return None
    
    except subprocess.TimeoutExpired:
        print(f"  [!] Таймаут при конвертации {json_path}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  [!] Ошибка: {e}", file=sys.stderr)
        return None

def create_all_in_one(all_cidrs):
    """Создание объединённого файла ALL-IN-ONE со всеми IP CIDR.
    
    Args:
        all_cidrs: Список всех IP CIDR от всех провайдеров
        
    Returns:
        str: Путь к созданному JSON файлу или None при ошибке
    """
    print(f"\n{'=' * 60}")
    print("Создание ALL-IN-ONE файла")
    print("=" * 60)
    
    if not all_cidrs:
        print("[!] ВНИМАНИЕ: Нет IP CIDR для объединения", file=sys.stderr)
        return None
    
    # Убираем дубликаты и сортируем
    unique_cidrs = sorted(set(all_cidrs))
    
    clash_data = {
        "version": 3,
        "rules": [
            {
                "ip_cidr": unique_cidrs
            }
        ]
    }
    
    # Создаём папку ALL-IN-ONE
    folder_path = os.path.join(OUTPUT_DIR, ALL_IN_ONE_DIR)
    os.makedirs(folder_path, exist_ok=True)
    
    # Сохраняем JSON файл
    filepath = os.path.join(folder_path, "all-in-one.json")
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(clash_data, f, indent=2, ensure_ascii=False)
    
    print(f"  [OK] Создан: {filepath}")
    print(f"      Всего уникальных IP CIDR: {len(unique_cidrs)}")
    
    return filepath

def main():
    """Главная функция - обработка всех провайдеров."""
    print("=" * 60)
    print("GitHub Actions: Автоматическое обновление IP-списков")
    print("=" * 60)
    
    providers = load_providers_config(PROVIDERS_CONFIG)
    
    if not providers:
        print("ОШИБКА: Нет провайдеров для обработки", file=sys.stderr)
        sys.exit(1)
    
    print(f"\nВсего провайдеров: {len(providers)}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    json_files = []
    all_cidrs = []  # Собираем все CIDR для ALL-IN-ONE
    
    for idx, (provider_name, asn_list) in enumerate(providers.items()):
        # Задержка между провайдерами для избежания rate limiting
        if idx > 0:
            print(f"\n⏳ Пауза 3 секунды...")
            time.sleep(3)
        
        json_path, cidrs = process_provider(provider_name, asn_list)
        if json_path:
            json_files.append(json_path)
            all_cidrs.extend(cidrs)  # Добавляем CIDR в общий список
    
    print(f"\n{'=' * 60}")
    print(f"JSON файлов создано: {len(json_files)}")
    
    # Создаём ALL-IN-ONE файл
    all_in_one_path = create_all_in_one(all_cidrs)
    if all_in_one_path:
        json_files.append(all_in_one_path)
    
    # Поиск sing-box бинарника
    singbox_bin = find_singbox_binary()
    
    if not singbox_bin:
        print(f"\n[!] ВНИМАНИЕ: sing-box не найден, конвертация в SRS пропущена")
        print(f"    Искал в: {', '.join(SINGBOX_PATHS)}")
        print("    JSON файлы созданы успешно")
        sys.exit(0)
    
    print(f"\n✓ sing-box найден: {singbox_bin}")
    
    print(f"\n{'=' * 60}")
    print("Конвертация JSON → SRS")
    print("=" * 60)
    
    srs_count = 0
    for json_path in json_files:
        if convert_json_to_srs(json_path, singbox_bin):
            srs_count += 1
    
    print(f"\n{'=' * 60}")
    print(f"Готово!")
    print(f"  JSON файлов: {len(json_files)}")
    print(f"  SRS файлов:  {srs_count}")
    print("=" * 60)

if __name__ == "__main__":
    main()
