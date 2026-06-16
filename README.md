```markdown
# Telegram Username Checker 🔍

A simple tool to check if a Telegram username is free or taken.
Built with Python and Telethon, optimized for users in Iran (supports SOCKS5 proxy).

## Requirements

- Python 3.x
- V2ray (or any SOCKS5 proxy) running on port `10808`

## Installation

pip install telethon python-socks

## Usage

1. Run the script:
python check.py

2. On first run, enter your phone number and the code Telegram sends you.

3. Enter usernames one by one (without @). Press Enter on an empty line to start checking.

## Output

Username             Status
-----------------------------------
@tanhatarin           FREE ✅
@darkrooh             TAKEN ❌
@biaramesh            INVALID ⚠️

- FREE ✅ — Username is available
- TAKEN ❌ — Username is already taken
- INVALID ⚠️ — Username doesn't meet Telegram's requirements

## Notes

- Your session is saved locally after first login — you won't need to log in again.
- Do NOT share or upload your `session.session` file.
- Make sure your proxy is running before executing the script.

---

# چک‌کننده یوزرنیم تلگرام 🔍

ابزاری ساده برای چک کردن اینکه آیا یوزرنیم تلگرام آزاده یا گرفته شده.
با پایتون و Telethon ساخته شده و برای کاربران ایرانی بهینه شده (پشتیبانی از پروکسی SOCKS5).

## پیش‌نیازها

- Python 3.x
- V2ray (یا هر پروکسی SOCKS5) روی پورت `10808`

## نصب

pip install telethon python-socks

## نحوه استفاده

1. اسکریپت رو اجرا کن:
python check.py

2. در اولین اجرا، شماره تلفن و کد تایید تلگرام رو وارد کن.

3. یوزرنیم‌ها رو یکی یکی وارد کن (بدون @). برای شروع چک کردن یه Enter خالی بزن.

## خروجی

یوزرنیم             وضعیت
-----------------------------------
@tanhatarin           FREE ✅
@darkrooh             TAKEN ❌
@biaramesh            INVALID ⚠️

- FREE ✅ — یوزرنیم آزاده
- TAKEN ❌ — یوزرنیم گرفته شده
- INVALID ⚠️ — یوزرنیم معتبر نیست (خیلی کوتاه، کاراکتر غیرمجاز و ...)

## نکات

- بعد از اولین لاگین، سشن ذخیره میشه و دیگه نیاز به لاگین مجدد نیست.
- فایل `session.session` رو به کسی نده و آپلود نکن.
- قبل از اجرای کد مطمئن شو پروکسیت روشنه.
```
