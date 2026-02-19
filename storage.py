# storage.py
import csv
import os
from datetime import datetime

STORAGE_FILE = "data/prices.csv"

def init_storage():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "price", "date"])

def save_price(name: str, price: float):
    with open(STORAGE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, price, datetime.now().strftime("%Y-%m-%d %H:%M")])

def get_last_price(name: str) -> float | None:
    if not os.path.exists(STORAGE_FILE):
        return None
    with open(STORAGE_FILE, "r") as f:
        rows = [row for row in csv.reader(f) if row[0] == name]
    if len(rows) < 2:  # ignore header
        return None
    return float(rows[-1][1])