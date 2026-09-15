# 🛍️ Wildberries Savdo va Logistika Infratuzilmasi Data Tahlili

Ushbu loyiha **Wildberries** marketplace platformasining 6 ta MDH davlatidagi **28,312 ta buyurtma berish punktlari (PVZ)** va **967 ta mahsuloti** bo'yicha to'liq ma'lumotlar tahlili (Data Analytics) portfolio loyihasidir.

Loyiha **Omonulla Toshpo'latov** tomonidan tayyorlangan bo'lib, **Excel ➔ Python ➔ PostgreSQL ➔ Power BI** to'liq ma'lumotlar zanjirini (pipeline) qamrab oladi.

---

## 👤 Muallif Bilan Bog'lanish

- **LinkedIn:** [Omonulla Toshpo'latov](https://www.linkedin.com/in/omonulla-toshpo-latov-8a45a9351/)
- **GitHub:** [@Toshpolatov12](https://github.com/Toshpolatov12)
- **Telegram:** [@toshpolatov12](https://t.me/toshpolatov12)

---

## 📌 Loyiha Maqsadi va Dolzarbligi

1. **Geografik Logistika Tahlili:** 28,312 ta PVZ punktining 6 ta davlat bo'yicha taqsimotini o'rganish va O'zbekiston kabi rivojlanayotgan bozorlardagi o'sish salohiyatini baholash.
2. **Narx va Chegirmalar Elastikligi:** Chegirma foizining savdo aylanmasiga ta'sirini o'rganish va optimal chegirma chegarasini aniqlash.
3. **Mijozlar Fikri va Ishonchi:** Mahsulot reytingi va sharhlar hajmining savdoni harakatlantiruvchi kuchini tahlil qilish.
4. **Relatsion Baza va Avtomatlashtirish:** PostgreSQL da jadvallarni o'zaro bog'lash (ERD) va ma'lumot kiritishdagi insoniy xatoliklarni formulalar orqali avtomatik to'g'rilovchi **Trigger funksiyalari**ni joriy etish.
5. **Interaktiv Hisobot:** Power BI da doimiy yangilanib turuvchi (Live Refresh) boshqaruv panelini ishlab chiqish.

---

## 📊 Asosiy Ko'rsatkichlar (KPIs)

| Ko'rsatkich | Qiymat | Izoh |
|---|---|---|
| **Umumiy PVZ Tarmog'i** | **28,312 ta** | Rossiya (26,569), Belarus (902), Qozog'iston (445), Armaniston (289), O'zbekiston (77), Qirg'iziston (30) |
| **Tahlil Qilingan Mahsulotlar** | **967 ta** | Turli xil toifadagi tovarlar namunasi |
| **O'rtacha Mijozlar Reytingi** | **4.70 / 5.00** | Yuqori mijozlar qoniqishi |
| **O'rtacha Chegirma Foizi** | **57%** | Agressiv marketing va ommaviy talab |
| **Asosiy Savdo Oralig'i** | **500 – 1,500 RUB** | Jami xaridlar hajmining 54% qismi |

---

## 🗂️ Loyiha Strukturasi

```text
wildberries-analytics/
├── index.html                # Interaktiv yagona sahifali veb-dashboard (O'zbek tilida)
├── assets/
│   └── images/               # Python, PostgreSQL va Power BI tahlil skrinshotlari (31 ta rasm)
├── data/
│   ├── raw/                  # Boshlang'ich Excel ma'lumotlar
│   └── processed/            # Tozalangan CSV ma'lumotlar
├── notebooks/                # Jupyter Notebook tahlil fayllari
├── scripts/                  # Python generator va tozalash skriptlari
└── README.md                 # Loyiha hujjati
```

---

## 🛠️ Qo'llanilgan Texnologiyalar

- **Python:** Pandas, NumPy, Matplotlib, Seaborn
- **Ma'lumotlar Bazasi:** PostgreSQL, PL/pgSQL Trigger Funksiyalari, pgAdmin4 ERD
- **Biznes Tahlil (BI):** Power BI (Live Database Connection)
- **Frontend / Dashboard:** Semantic HTML5, Tailwind CSS, Lucide Icons, ApexCharts

---

## 💡 Asosiy Xulosalar & Biznes Tavsiyalari

1. **O'zbekiston — Asosiy O'sish Bozori:** 36M+ aholiga nisbatan hozircha atigi 77 ta PVZ mavjud. Bu bozor eng yuqori foydalanilmagan logistika zaxirasiga ega.
2. **Optimal Chegirma Nuqtasi (~47%):** 47% atrofidagi chegirmalar talabni maksimal darajada oshiradi. 60%+ chegirmalar esa sof marjaning pasayishiga olib keladi.
3. **Fulfillment (FBO vs FBS):** 500–1,500 RUB oraliqdagi tez aylanuvchi tovarlar uchun FBO (Wildberries ombori) eng yaxshi tanlov, qimmat va og'ir mebellar uchun esa FBS (o'z omboringiz) saqlash harajatlarini sezilarli tejaydi.
4. **PostgreSQL Triggerlari:** Ma'lumot kiritishda ustunlarning hatto yarmi to'ldirilsa ham, triggerlar qolgan barcha ko'rsatkichlarni avtomatik hisoblab to'g'rilaydi.

---

## 🌐 Dashboardni Ishga Tushirish

Dashboard hech qanday maxsus server yoki murakkab o'rnatish talab qilmaydi. Shunchaki `index.html` faylini brauzerda ochish kifoya:

```bash
# Brauzerda ochish
Start-Process index.html
```
