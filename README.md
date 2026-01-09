<div align="center">

# 🌐 IP-Ranger

### Автоматически обновляемые списки IP-подсетей для обхода блокировок

[![GitHub stars](https://img.shields.io/github/stars/mudachyo/IP-Ranger)](https://github.com/mudachyo/IP-Ranger/stargazers)
[![Last Updated](https://img.shields.io/badge/обновление-ежедневно-brightgreen)](https://github.com/mudachyo/IP-Ranger)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

> 🕐 **Последнее обновление:** <!-- LAST_UPDATED -->2026-01-09 03:52:01 UTC<!-- /LAST_UPDATED -->

</div>

---

## 📖 Что это?

**IP-Ranger** — это готовое решение для тех, кто использует [Podkop](https://podkop.net/) на OpenWrt или sing-box для маршрутизации трафика через VPN/прокси.

### 🎯 Зачем это нужно?

Вместо того чтобы вручную искать и копировать IP-адреса заблокированных сервисов (Cloudflare, AWS, Google Cloud и др.), вы просто добавляете ссылку на наш список — и **всегда получаете актуальные данные**!

---

## 📥 Доступные списки

### 🎁 ALL-IN-ONE

**Все провайдеры в одном файле**

```
https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/ALL-IN-ONE/all-in-one.srs
```

### 📋 Список по провайдерам

<br>

| 🏢 Провайдер | 🔢 ASN | 📦 SRS файл | 📄 JSON файл |
|-------------|--------|------------|--------------|
| **Akamai** | AS12222, AS16625, AS20940, AS63949, AS32787, AS31108 | [📥 akamai.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/akamai/akamai.srs) | [📄 akamai.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/akamai/akamai.json) |
| **Alibaba Cloud** | AS45102, AS37963, AS24429 | [📥 alibaba.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/alibaba/alibaba.srs) | [📄 alibaba.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/alibaba/alibaba.json) |
| **AWS** | AS16509, AS14618, AS8987 | [📥 aws.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/aws/aws.srs) | [📄 aws.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/aws/aws.json) |
| **CDN77** | AS60068 | [📥 cdn77.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/cdn77/cdn77.srs) | [📄 cdn77.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/cdn77/cdn77.json) |
| **Cloudflare** | AS13335, AS209242, AS395747, AS202623 | [📥 cloudflare.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/cloudflare/cloudflare.srs) | [📄 cloudflare.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/cloudflare/cloudflare.json) |
| **Constant (Vultr)** | AS20473 | [📥 constant.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/constant/constant.srs) | [📄 constant.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/constant/constant.json) |
| **Contabo** | AS51167 | [📥 contabo.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/contabo/contabo.srs) | [📄 contabo.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/contabo/contabo.json) |
| **DigitalOcean** | AS14061 | [📥 digitalocean.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/digitalocean/digitalocean.srs) | [📄 digitalocean.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/digitalocean/digitalocean.json) |
| **Fastly** | AS54113 | [📥 fastly.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/fastly/fastly.srs) | [📄 fastly.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/fastly/fastly.json) |
| **Google Cloud** | AS15169, AS396982, AS394089, AS36040 | [📥 google.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/google/google.srs) | [📄 google.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/google/google.json) |
| **Hetzner** | AS24940 | [📥 hetzner.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/hetzner/hetzner.srs) | [📄 hetzner.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/hetzner/hetzner.json) |
| **Huawei Cloud** | AS4809 | [📥 huawei.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/huawei/huawei.srs) | [📄 huawei.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/huawei/huawei.json) |
| **Ionos** | AS8560 | [📥 ionos.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/ionos/ionos.srs) | [📄 ionos.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/ionos/ionos.json) |
| **Microsoft Azure** | AS8075 | [📥 microsoft.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/microsoft/microsoft.srs) | [📄 microsoft.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/microsoft/microsoft.json) |
| **Oracle** | AS31898 | [📥 oracle.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/oracle/oracle.srs) | [📄 oracle.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/oracle/oracle.json) |
| **OVH** | AS16276, AS35540 | [📥 ovh.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/ovh/ovh.srs) | [📄 ovh.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/ovh/ovh.json) |
| **Scaleway** | AS12876 | [📥 scaleway.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/scaleway/scaleway.srs) | [📄 scaleway.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/scaleway/scaleway.json) |
| **Tencent Cloud** | AS132203 | [📥 tencent.srs](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/tencent/tencent.srs) | [📄 tencent.json](https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/tencent/tencent.json) |

---

## 🚀 Podkop на OpenWrt

### Шаг 1: Выберите нужный список

Выберите конкретный провайдер из таблицы выше.

### Шаг 2: Добавьте список в Podkop

1. **Откройте веб-интерфейс** OpenWrt (обычно http://192.168.1.1)
2. Перейдите в **Services** → **Podkop**
3. Выберите нужную **секцию** (например, Main)
4. Найдите раздел **"Внешние списки подсетей"** (Remote Subnet Lists)
5. В поле **URL** вставьте скопированную ссылку
6. Нажмите **Save & Apply**

### Шаг 3: Готово! 🎉

Podkop автоматически загрузит список и начнёт направлять трафик через указанный туннель/прокси.

---

## 🔧 Использование в sing-box

Для пользователей sing-box вы можете использовать списки напрямую в конфигурации:

### Пример конфигурации

```json
{
  "route": {
    "rule_set": [
      {
        "type": "remote",
        "tag": "cloudflare-ips",
        "format": "binary",
        "url": "https://raw.githubusercontent.com/mudachyo/IP-Ranger/main/ip-lists/cloudflare/cloudflare.srs",
        "download_detour": "direct"
      }
    ],
    "rules": [
      {
        "rule_set": "cloudflare-ips",
        "outbound": "proxy"
      }
    ]
  }
}
```

---

## 📊 Форматы файлов

| Формат | Описание | Когда использовать |
|--------|----------|-------------------|
| **`.srs`** | Бинарный формат sing-box ruleset | ✅ Рекомендуется для Podkop и sing-box |
| **`.json`** | Текстовый JSON с массивом IP-подсетей | Для ручной обработки или других инструментов |

---

## ❓ Часто задаваемые вопросы

<details>
<summary><b>🤔 Как часто обновляются списки?</b></summary>
Списки обновляются автоматически каждый день в 5:00 по Москве через GitHub Actions. Время последнего обновления указано вверху страницы.
</details>

<details>
<summary><b>🌐 Что такое ASN?</b></summary>
ASN (Autonomous System Number) — это уникальный номер, который присваивается провайдеру интернет-услуг. По ASN мы определяем все IP-подсети, принадлежащие конкретному провайдеру.
</details>

<details>
<summary><b>💾 Можно ли скачать список и использовать локально?</b></summary>
Да, но тогда вы потеряете автоматические обновления. Лучше использовать прямые ссылки на GitHub — Podkop сам будет загружать актуальные версии.
</details>

<details>
<summary><b>🔒 Это безопасно?</b></summary>
Да! Весь код открыт и доступен на GitHub. Списки генерируются из официальных источников (IPInfo API) и не содержат никаких вредоносных данных.
</details>

<details>
<summary><b>📝 Могу ли я добавить свой провайдер?</b></summary>
Конечно! Откройте Issue на GitHub или сделайте Pull Request с изменениями в файле <code>providers.json</code>.
</details>

<details>
<summary><b>🔍 Как проверить, какие сервисы блокирует мой провайдер?</b></summary>
Используйте <a href="https://hyperion-cs.github.io/dpi-checkers/ru/tcp-16-20/" target="_blank">DPI-чекер от Hyperion</a> — он покажет, какие сервисы и протоколы блокируются на уровне DPI (Deep Packet Inspection) вашим интернет-провайдером. Это поможет понять, какие списки IP вам нужны.
</details>

---

## 🌟 Поддержите проект

Если этот проект помог вам, поставьте ⭐ на GitHub!

<a href="https://www.star-history.com/#mudachyo/IP-Ranger&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=mudachyo/IP-Ranger&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=mudachyo/IP-Ranger&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=mudachyo/IP-Ranger&type=date&legend=top-left" />
 </picture>
</a>

---

## 📚 Полезные ссылки

- 📖 [Документация Podkop](https://podkop.net/)
- 🔧 [Документация sing-box](https://sing-box.sagernet.org/)
- 📋 [sing-box Rule Sets](https://sing-box.sagernet.org/configuration/rule-set/)
- 🌐 [IPInfo API](https://ipinfo.io/)

---

## 📄 Лицензия

MIT License - используйте свободно в личных и коммерческих проектах!

---

<div align="center">

**Made with ❤️ by from Russia**

[⬆ Наверх](#-ip-ranger)

</div>
