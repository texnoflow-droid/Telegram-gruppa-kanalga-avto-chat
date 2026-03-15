# 🚀 Telegram Auto-File Sender (Telethon)

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Telethon](https://img.shields.io/badge/Library-Telethon-orange?style=for-the-badge&logo=telegram)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Ushbu loyiha **Telethon** kutubxonasi yordamida Telegram kanallari yoki guruhlariga rasm va fayllarni avtomatik, takroriy tarzda yuborish uchun ishlab chiqilgan. Barcha maxfiy kalitlar xavfsizlik maqsadida `.env` faylida saqlanadi.

---

## 🎯 Nega aynan bu loyiha?

* **Avtomatizatsiya:** Ma'lum bir vaqt oralig'ida fayllarni tinimsiz jo'natish.
* **Xavfsizlik:** API kalitlari va shaxsiy ma'lumotlar kod ichida emas, balki atrof-muhit o'zgaruvchilarida (`.env`) saqlanadi.
* **Yengillik:** Minimal resurs talab qiladi va oson sozlanadi.
* **Flood Control:** Telegram cheklovlariga (rate limit) tushib qolmaslik uchun aqlli kechiktirish tizimi.

---

## ✨ Asosiy imkoniyatlar

- [x] `.env` orqali xavfsiz konfiguratsiya.
- [x] Telethon yordamida barqaror ulanish (UserBot).
- [x] Fayllarni cheksiz tsiklda yuborish rejimi.
- [x] Avtomatik sessiya boshqaruvi.

---

## 🛠 Texnik talablar

Loyihani ishga tushirishdan oldin tizimingizda quyidagilar mavjudligiga ishonch hosil qiling:
* **Python:** 3.10 yoki undan yuqori versiya.
* **Telegram API:** [my.telegram.org](https://my.telegram.org) orqali olingan `API_ID` va `API_HASH`.
* **Chat ID:** Fayl yuborilishi kerak bo'lgan kanal yoki guruhning identifikatori (odatda `-100` bilan boshlanadi).

---

## ⚙️ O'rnatish va Sozlash

### 1. Loyihani yuklab olish
```bash
git clone [https://github.com/texnoflow-droid/Telegram-gruppa-kanalga-avto-chat.git](https://github.com/texnoflow-droid/Telegram-gruppa-kanalga-avto-chat.git)
cd Telegram-gruppa-kanalga-avto-chat

├── main.py              # Asosiy logika va ishga tushirish
├── requirements.txt     # Kerakli kutubxonalar ro'yxati
├── .env                 # Maxfiy sozlamalar (Local)
├── .env.example         # Sozlamalar namunasi
├── .gitignore           # Git uchun istisno fayllar
└── README.md            # Loyiha qo'llanmasi
