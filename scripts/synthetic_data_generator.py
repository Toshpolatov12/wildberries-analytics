"""
Wildberries Synthetic Data Generator
------------------------------------
Ushbu skript tahlil va test qilish uchun 1200+ ta realistik Wildberries 
mahsulotlari ma'lumotlarini (xom holatda) hosil qiladi va data/raw papkasiga saqlaydi.
Standard Python kutubxonalari (csv, random, math) bilan ham to'liq ishlaydi.
"""

import os
import csv
import random
import math
from datetime import datetime, timedelta

def generate_wildberries_data(num_records=1200, output_path=None):
    random.seed(42)

    categories = {
        "Kiyim va poyabzal": [
            "Erkaklar futbolkasi Basic", "Ayollar ko'ylagi Vintage", "Krossovka Sport Run",
            "Jinsi shim Slim Fit", "Qishki kurtka Oversize", "Klassik kostyum-shim",
            "Uy shippagi Soft", "Charm kamar", "Sviter Casual", "Paypoqlar to'plami (5 juft)"
        ],
        "Elektronika": [
            "Simsiz quloqchin TWS", "Smart soat Pro", "Powerbank 20000mAh",
            "Telefon g'ilofi Silikon", "USB Type-C kabel Tezkor", "Bluetooth karnay Mini",
            "Mexanik klaviatura RGB", "Simsiz sichqoncha", "Avtomobil ushlagichi", "Ring Light lampa"
        ],
        "Go'zallik va parvarish": [
            "Yuz kremi Namlantiruvchi", "Shampun Sulfatsiz", "Lab bo'yog'i Matte",
            "Yuz zardobi Hyaluron", "Parfyum Elixir 50ml", "Tana skrabı Kofe",
            "Qo'l kremi Mini", "Soch maskasi Keratin", "Quyoshdan himoya kremi SPF50", "Tish tozalovchi kukun"
        ],
        "Uy-ro'zg'or buyumlari": [
            "Mikrofibra sochiqlar to'plami", "Oshxona pichoqlar to'plami", "Yostiq Ortopedik",
            "Termos 1L zanglamas", "Organayzer javon", "Havo tozalagich diffuzor",
            "Bokal to'plami (6 dona)", "Oshxona tarozisi Elektron", "Choyshablar to'plami Satina", "Idish yuvish geli 1L"
        ],
        "Bolalar tovarlari": [
            "Konstruktor Lego mos keluvchi", "Yumshoq ayiqcha Plush", "Chizmachilik to'plami 100+ dona",
            "Bolalar kolyaskasi Yengil", "Rivojlantiruvchi taxta Busyboard", "Bolalar butilkasi Anti-kolik",
            "Plastilin to'plami", "Bolalar futbolkasi Paxta", "Pampers to'plami XL", "Masofadan boshqariladigan mashina"
        ],
        "Sport va dam olish": [
            "Fitnes rezinkalar to'plami", "Yoga mat 6mm", "Gantellar to'plami 2x5kg",
            "Sport sumkasi Suv o'tkazmaydigan", "Velosiped chirog'i LED", "Sakrash arqoni Metall simli",
            "Termo ichki kiyim", "Suv idishi Sport 750ml", "Shaker Protein", "Taktik ryukzak 40L"
        ]
    }

    category_list = list(categories.keys())
    weights = [0.25, 0.20, 0.20, 0.15, 0.10, 0.10]
    
    data = []
    start_date = datetime.now() - timedelta(days=365)

    for i in range(1, num_records + 1):
        product_id = f"WB-{100000 + i}"
        cat = random.choices(category_list, weights=weights, k=1)[0]
        product_name = random.choice(categories[cat])

        if cat == "Elektronika":
            price = round(random.uniform(80000, 1800000), -3)
        elif cat == "Kiyim va poyabzal":
            price = round(random.uniform(60000, 950000), -3)
        elif cat == "Bolalar tovarlari":
            price = round(random.uniform(45000, 600000), -3)
        elif cat == "Uy-ro'zg'or buyumlari":
            price = round(random.uniform(30000, 750000), -3)
        elif cat == "Sport va dam olish":
            price = round(random.uniform(40000, 650000), -3)
        else: # Go'zallik
            price = round(random.uniform(25000, 450000), -3)

        discount_percent = int(max(5, min(80, random.gauss(35, 15))))
        rating = round(max(2.5, min(5.0, random.gauss(4.5, 0.35))), 1)
        reviews_count = int(min(3500, random.expovariate(1/120)))
        
        orders_base = (reviews_count * random.uniform(3.5, 8.0)) + (discount_percent * 12) + (rating * 40)
        orders_count = int(max(5, min(25000, orders_base + random.gauss(50, 20))))
        
        seller_rating = round(max(3.0, min(5.0, random.gauss(4.6, 0.25))), 1)
        stock_quantity = random.choice([0, 10, 25, 50, 100, 250, 500])

        random_days = random.randint(0, 365)
        added_date = (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

        # Xom ma'lumotlar uchun missing value kiritamiz
        price_val = price if random.random() >= 0.02 else ""
        rating_val = rating if random.random() >= 0.015 else ""

        data.append({
            "product_id": product_id,
            "product_name": product_name,
            "category": cat,
            "price": price_val,
            "discount_percent": discount_percent,
            "rating": rating_val,
            "reviews_count": reviews_count,
            "orders_count": orders_count,
            "seller_rating": seller_rating,
            "stock_quantity": stock_quantity,
            "date_added": added_date
        })

    # Dublikat qatorlar qo'shish
    duplicates = random.sample(data, 10)
    data.extend(duplicates)

    if output_path is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(current_dir, "..", "data", "raw", "wildberries_raw_data.csv")

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    headers = list(data[0].keys())
    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"[OK] {len(data)} ta ma'lumot muvaffaqiyatli generatsiya qilindi va '{output_path}' ga saqlandi!")

if __name__ == "__main__":
    generate_wildberries_data()
