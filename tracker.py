# tracker.py
import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, PRODUCTS
from scraper import get_price
from storage import init_storage, save_price, get_last_price

def send_telegram(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    })

def check_prices():
    init_storage()
    
    for product in PRODUCTS:
        print(f"Vérification du prix : {product['name']}...")
        
        current_price = get_price(product["url"])
        
        if current_price is None:
            print("Prix non récupéré, on passe.")
            continue
        
        last_price = get_last_price(product["name"])
        save_price(product["name"], current_price)
        
        print(f"Prix actuel : {current_price}€ | Prix précédent : {last_price}€")
        
        # Alerte si prix en baisse
        if last_price and current_price < last_price:
            send_telegram(
                f"📉 Baisse de prix détectée !\n\n"
                f"🖥️ {product['name']}\n"
                f"💰 Ancien prix : {last_price}€\n"
                f"✅ Nouveau prix : {current_price}€\n"
                f"💸 Économie : {round(last_price - current_price, 2)}€\n"
                f"🔗 {product['url']}"
            )
        
        # Alerte si prix sous le seuil cible
        if current_price < product["target_price"]:
            send_telegram(
                f"🎯 Prix cible atteint !\n\n"
                f"🖥️ {product['name']}\n"
                f"✅ Prix actuel : {current_price}€\n"
                f"🎯 Ton seuil : {product['target_price']}€\n"
                f"🔗 {product['url']}"
            )

if __name__ == "__main__":
    check_prices()


import schedule
import time

if __name__ == "__main__":
    check_prices()  # lancer une fois au démarrage
    schedule.every().day.at("08:00").do(check_prices)
    while True:
        schedule.run_pending()
        time.sleep(60)