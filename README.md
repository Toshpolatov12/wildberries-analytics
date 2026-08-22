# 🛍️ Wildberries E-commerce Sales & Product Analytics

Ushbu loyiha **Wildberries** marketplace platformasidagi mahsulotlar savdosi, narx strategiyasi, chegirmalar va mijozlar talabi o'rtasidagi bog'liqlikni tahlil qilishga qaratilgan **Data Analytics** portfolio loyihasidir.

---

## 📌 Loyiha Maqsadi
- Wildberries platformasidagi turli kategoriyalar bo'yicha sotuvlar va tushumni tahlil qilish.
- Chegirma foizining xaridlar soniga ta'sirini o'rganish.
- Mahsulot reytingi va sharhlar (Social Proof) savdo hajmiga qanday ta'sir qilishini aniqlash.
- Marketplace sotuvchilari uchun ma'lumotlarga asoslangan (Data-Driven) biznes tavsiyalar ishlab chiqish.

---

## 🗂️ Loyiha Strukturasi

```text
wildberries-analytics/
├── data/
│   ├── raw/                  # Xom (boshlang'ich) ma'lumotlar to'plami
│   │   └── wildberries_raw_data.csv
│   └── processed/            # Tozalangan va hisoblangan ma'lumotlar
│       └── wildberries_cleaned_data.csv
├── notebooks/
│   └── wildberries_eda.ipynb # Vizualizatsiya va EDA (Jupyter Notebook)
├── scripts/
│   ├── synthetic_data_generator.py # 1000+ qatorli realistik ma'lumot yaratuvchi skript
│   ├── data_cleaning.py           # Ma'lumotlarni tozalash va tayyorlash
│   └── analysis.py                # Asosiy biznes ko'rsatkichlari va tahlil
├── requirements.txt          # Kerakli Python kutubxonalari
└── README.md                 # Loyiha hujjatlari
```

---

## 🛠️ Qo'llanilgan Texnologiyalar
- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **Jupyter Notebook** (Eksplorativ tahlil va vizualizatsiya)
- **Data Preprocessing & Feature Engineering**
- **Statistical Analysis & Correlation**

---

## 📊 Asosiy Xulosalar (Key Insights)

1. **Top Kategoriyalar:** `Elektronika` va `Kiyim va poyabzal` kategoriyalari umumiy tushumning **60% dan ortig'ini** ta'minlaydi.
2. **Chegirma Samaradorligi:** 30% - 50% oralig'idagi chegirmalar sotuv hajmini sezilarli darajada oshiradi, ammo 60%+ chegirmalar marjaning kamayishiga olib kelishi mumkin.
3. **Ijtimoiy Isbot (Social Proof):** Sharhlar soni va mahsulot reytingi buyurtmalar soni bilan to'g'ridan-to'g'ri bog'liq (yuqori korrelyatsiya).
4. **Reyting chegarasi:** 4.5+ reytingga ega mahsulotlar o'rtacha past reytinglilarga nisbatan 2 barobardan ko'proq buyurtma oladi.

---

## 🚀 Loyihani Ishga Tushirish (How to Run)

### 1. Repozitoriyani ochish va kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 2. Ma'lumotlarni generatsiya qilish (Synthetic Data)
```bash
python scripts/synthetic_data_generator.py
```

### 3. Ma'lumotlarni tozalash (Data Cleaning)
```bash
python scripts/data_cleaning.py
```

### 4. Konsol orqali tezkor tahlilni ko'rish
```bash
python scripts/analysis.py
```

### 5. Jupyter Notebook da to'liq vizual tahlilni ochish
```bash
jupyter notebook notebooks/wildberries_eda.ipynb
```

---

## 👤 Muallif
Data Analytics Portfolio Project
