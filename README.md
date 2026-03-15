 # Telegram Fayl Yuboruvchi (Telethon)
 
 Ushbu loyiha Telethon kutubxonasi yordamida Telegram kanal yoki guruhga rasm/fayllarni avtomatik va takroriy tarzda yuborish uchun mo‘ljallangan. Maxfiy ma’lumotlar `.env` faylida saqlanadi, versiya nazoratiga kirmaydi.
 
 ## Nega kerak?
 - Doimiy ravishda ma’lum fayllarni kanalingiz/guruhingizga jo‘natish.
 - Oddiy sozlash va ishga tushirish.
 - Maxfiy kalitlarni (API ID/HASH, telefon, kanal ID) koddan ajratib saqlash.
 
 ## Asosiy imkoniyatlar
 - `.env` orqali xavfsiz konfiguratsiya
 - Telethon yordamida ishonchli ulanish
 - Fayllarni cheksiz siklda jo‘natish
 - Flood control ehtiyotkorligi (kechiktirish)
 
 ## Talablar
 - Python 3.10 yoki yangiroq
 - Telegram API ma’lumotlari (API ID, API HASH) — my.telegram.org
 - Telegram hisobingiz telefoni
 - Kanal/Guruh ID (supergroup/channel uchun odatda manfiy son: `-100...`)
 
 ## O‘rnatish
 1. Loyihani klonlang yoki papkani tayyorlang.
 2. Virtual muhit yarating (ixtiyoriy, ammo tavsiya etiladi).
 
 Windows (PowerShell) misol:
 
 ```bash
 python -m venv .venv
 .venv\Scripts\activate
 pip install -r requirements.txt
 ```
 
 ## Sozlash (.env)
 `.env.example` faylini nusxa ko‘chirib `.env` qilib to‘ldiring:
 
 ```env
 API_ID=123456
 API_HASH=your_api_hash
 PHONE_NUMBER=+9989XXXXXXX
 CHANNEL_ID=-1002816614203
 ```
 
 Izohlar:
 - `API_ID` va `API_HASH` — my.telegram.org saytidan olinadi.
 - `PHONE_NUMBER` — +kod bilan (masalan, +9989...) kiritiladi.
 - `CHANNEL_ID` — supergroup/channel uchun odatda manfiy son bo‘ladi. Agar username mavjud bo‘lsa, uni ham ishlatish mumkin.
 
 ## Ishga tushirish
 
 ```bash
 python main.py
 ```
 
 Birinchi ishga tushirishda Telethon sessiya yaratishi va tasdiqlash kodini so‘rashi mumkin — konsolda ko‘rsatmalarga amal qiling. Sessiya fayli `.session` ko‘rinishida yaratiladi va `.gitignore` uni repository’ga kiritmaydi.
 
 ## Qanday ishlaydi
 - [main.py](file:///c:/Users/Laptop/Desktop/Telegram%20gruppa/main.py) fayli `.env` dan konfiguratsiyani o‘qiydi.
 - Telethon `client.start(phone=PHONE_NUMBER)` orqali hisobga ulanadi.
 - `files` ro‘yxatidagi har bir fayl mavjud bo‘lsa, `CHANNEL_ID` ga yuboriladi.
 - Sikl takroran ishlaydi va har yuborish orasida 1 soniya kutadi (flood control uchun ko‘proq kutish tavsiya etiladi).
 
 ## Loyihaning tuzilmasi
 - [main.py](file:///c:/Users/Laptop/Desktop/Telegram%20gruppa/main.py) — asosiy ishga tushirish fayli
 - [requirements.txt](file:///c:/Users/Laptop/Desktop/Telegram%20gruppa/requirements.txt) — bog‘liqliklar ro‘yxati (Telethon, python-dotenv)
 - [.env.example](file:///c:/Users/Laptop/Desktop/Telegram%20gruppa/.env.example) — namunaviy sozlamalar
 - [.gitignore](file:///c:/Users/Laptop/Desktop/Telegram%20gruppa/.gitignore) — maxfiy va lokal fayllarni e’tiborsiz qoldirish
 
 ## Xavfsizlik bo‘yicha eslatmalar
 - `.env` faylini hech qachon commit qilmang — unda maxfiy kalitlar bor.
 - Telethon sessiya fayllari (`*.session`, `*.session-journal`) ham commit qilinmaydi.
 - Agar maxfiy ma’lumotlar ilgari kodga yozib qo‘yilgan bo‘lsa, ularni darhol almashtiring (rotate).
 
 ## Flood control (rate limit) haqida
 Telegram API haddan tashqari tez-tez xabar yuborishni cheklaydi. Skriptda 1 soniyalik kutish bor, ammo amaliyotda 30–60 soniya kutish tavsiya qilinadi. Ko‘p fayl yuborilsa, kechiktirishni oshiring.
 
 ## Tez-tez uchraydigan savollar
 - “CHANNEL_ID ni qayerdan olaman?” — Telegram ichida botlar/oraliq vositalar orqali yoki kanal havolasidan ID ni topish mumkin; supergruh/kanal ID ko‘pincha `-100...` bilan boshlanadi.
 - “Birinchi ishga tushirishda nega kod so‘raydi?” — Telegram hisobni tasdiqlash uchun. Bu tabiiy, sessiya yaratiladi.
 - “Fayl topilmadi xabari chiqsa?” — Fayl nomi va joylashuvi to‘g‘ri ekanini tekshiring.
 
 ## GitHub’ga joylash (qisqa)
 1. `git init && git add . && git commit -m "Initial commit"`
 2. GitHub’da bo‘sh repository yarating.
 3. `git remote add origin https://github.com/<USER>/<REPO>.git`
 4. `git branch -M main && git push -u origin main`
 
 ---
 Agar xohlasangiz, GitHub’ga push qilish jarayonini ham birga bajarib beramiz.
 
