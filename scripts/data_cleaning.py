"""
Wildberries Data Cleaning & Preprocessing Script
------------------------------------------------
Ushbu skript xom ma'lumotlarni o'qiydi, tozalaydi, bo'sh qiymatlarni to'ldiradi,
yangi hisoblangan ustunlarni (Feature Engineering) qo'shadi va tozalangan faylni saqlaydi.
"""

import os
import csv
from datetime import datetime

def clean_wildberries_data(input_path=None, output_path=None):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if input_path is None:
        input_path = os.path.join(current_dir, "..", "data", "raw", "wildberries_raw_data.csv")
    if output_path is None:
        output_path = os.path.join(current_dir, "..", "data", "processed", "wildberries_cleaned_data.csv")

    print("--- 1. Ma'lumotlarni yuklash boshlandi ---")
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Xom fayl topilmadi: {input_path}")

    # Agar pandas o'rnatilgan bo'lsa pandas bilan, aks holda standart csv bilan ishlaydi
    try:
        import pandas as pd
        df = pd.read_csv(input_path)
        initial_len = len(df)
        print(f"Boshlang'ich qatorlar soni: {initial_len}, Ustunlar: {df.shape[1]}")

        # Dublikatlarni o'chirish
        df = df.drop_duplicates(subset=["product_id"], keep="first")
        print(f"[+] Dublikatlar olib tashlandi: {initial_len - len(df)} ta qator.")

        # Bo'sh qiymatlarni to'ldirish
        df["price"] = df.groupby("category")["price"].transform(lambda x: x.fillna(x.median()))
        df["rating"] = df["rating"].fillna(df["rating"].median())

        # Tiplarni to'g'rilash
        df["discount_percent"] = df["discount_percent"].astype(int)
        df["reviews_count"] = df["reviews_count"].astype(int)
        df["orders_count"] = df["orders_count"].astype(int)
        df["stock_quantity"] = df["stock_quantity"].astype(int)

        # Yangi hisoblangan ustunlar (Feature Engineering)
        df["final_price"] = (df["price"] * (1 - df["discount_percent"] / 100)).round(-2).astype(int)
        df["discount_amount"] = (df["price"] - df["final_price"]).astype(int)
        df["estimated_revenue"] = (df["final_price"] * df["orders_count"]).astype(int)
        df["review_per_order_ratio"] = (df["reviews_count"] / df["orders_count"]).round(4)
        
        # Segmentatsiya
        df["popularity_segment"] = pd.qcut(
            df["orders_count"],
            q=3,
            labels=["Kam sotilgan", "O'rtacha sotilgan", "Top sotilgan (Bestseller)"]
        )

        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        df.to_csv(output_path, index=False, encoding="utf-8")
        print(f"[OK] Tozalash muvaffaqiyatli yakunlandi (Pandas)! Natija: {output_path}")
        print(f"Yakuniy dataset o'lchami: {df.shape[0]} qator, {df.shape[1]} ustun.")
        return df

    except ImportError:
        # Fallback agar pandas o'rnatilmagan bo'lsa
        rows = []
        with open(input_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)

        initial_len = len(rows)
        print(f"Boshlang'ich qatorlar soni: {initial_len}")

        # 1. Dublikatlarni o'chirish
        seen_ids = set()
        unique_rows = []
        for r in rows:
            if r["product_id"] not in seen_ids:
                seen_ids.add(r["product_id"])
                unique_rows.append(r)

        print(f"[+] Dublikatlar olib tashlandi: {initial_len - len(unique_rows)} ta qator.")

        # 2. Median narx va reytinglarni hisoblash
        cat_prices = {}
        all_ratings = []
        for r in unique_rows:
            cat = r["category"]
            if r["price"]:
                cat_prices.setdefault(cat, []).append(float(r["price"]))
            if r["rating"]:
                all_ratings.append(float(r["rating"]))

        median_prices = {c: sorted(p)[len(p)//2] for c, p in cat_prices.items()}
        median_rating = sorted(all_ratings)[len(all_ratings)//2] if all_ratings else 4.5

        # 3. Tozalash va hisoblash
        cleaned_rows = []
        for r in unique_rows:
            price = float(r["price"]) if r["price"] else median_prices.get(r["category"], 150000.0)
            rating = float(r["rating"]) if r["rating"] else median_rating
            discount = int(float(r["discount_percent"]))
            reviews = int(float(r["reviews_count"]))
            orders = int(float(r["orders_count"]))
            stock = int(float(r["stock_quantity"]))

            final_price = int(round(price * (1 - discount / 100), -2))
            discount_amount = int(price - final_price)
            estimated_revenue = int(final_price * orders)
            ratio = round(reviews / orders, 4) if orders > 0 else 0.0

            r["price"] = int(price)
            r["discount_percent"] = discount
            r["rating"] = rating
            r["reviews_count"] = reviews
            r["orders_count"] = orders
            r["stock_quantity"] = stock
            r["final_price"] = final_price
            r["discount_amount"] = discount_amount
            r["estimated_revenue"] = estimated_revenue
            r["review_per_order_ratio"] = ratio

            cleaned_rows.append(r)

        # Segmentatsiyani hisoblash
        all_orders = sorted([r["orders_count"] for r in cleaned_rows])
        q1 = all_orders[len(all_orders)//3]
        q2 = all_orders[(2 * len(all_orders))//3]

        for r in cleaned_rows:
            if r["orders_count"] <= q1:
                r["popularity_segment"] = "Kam sotilgan"
            elif r["orders_count"] <= q2:
                r["popularity_segment"] = "O'rtacha sotilgan"
            else:
                r["popularity_segment"] = "Top sotilgan (Bestseller)"

        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        headers = list(cleaned_rows[0].keys())
        with open(output_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(cleaned_rows)

        print(f"[OK] Tozalash muvaffaqiyatli yakunlandi! Natija: {output_path}")
        print(f"Yakuniy dataset o'lchami: {len(cleaned_rows)} qator, {len(headers)} ustun.")

if __name__ == "__main__":
    clean_wildberries_data()
