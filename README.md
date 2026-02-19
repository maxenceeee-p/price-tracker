# Ìªí Price Tracker ‚Äî Automated Price Monitoring with Telegram Alerts

Automated price tracker built with Python and Playwright. Monitors product prices on Cdiscount, stores price history in a CSV file, and sends Telegram alerts when a price drops or reaches a target threshold. Runs daily via a built-in scheduler.

---

## ‚ú® Features

- **Automated scraping** ‚Äî uses Playwright to bypass JavaScript-heavy pages and anti-bot protections
- **Price history** ‚Äî stores all price records in a local CSV file for historical tracking
- **Dual Telegram alerts** ‚Äî notifies you when a price drops OR when it reaches your target threshold
- **Multi-product support** ‚Äî track multiple products simultaneously with a single config file
- **Daily scheduler** ‚Äî runs automatically every day at 8:00 AM, no manual action required

---

## Ì≥∏ Demo

**Terminal output:**
```
V√©rification du prix : Gigabyte RTX 5080 Wind...
Prix actuel : 1549.99‚Ç¨ | Prix pr√©c√©dent : 1599.99‚Ç¨
```

**Telegram alert:**
```
Ì≥â Baisse de prix d√©tect√©e !

Ì∂•Ô∏è Gigabyte RTX 5080 Wind
Ì≤∞ Ancien prix : 1599.99‚Ç¨
‚úÖ Nouveau prix : 1549.99‚Ç¨
Ì≤∏ √âconomie : 50.0‚Ç¨
Ì¥ó https://www.cdiscount.com/...
```

---

## Ìª†Ô∏è Tech Stack

| Tool | Usage |
|------|-------|
| Python 3.10+ | Core language |
| Playwright | Browser automation & scraping |
| CSV | Price history storage |
| Telegram Bot API | Real-time alerts |
| Schedule | Daily automation |

---

## Ì≥Å Project Structure

```
price-tracker/
‚îÇ
‚îú‚îÄ‚îÄ config.py         # Products URLs, Telegram credentials, target prices
‚îú‚îÄ‚îÄ scraper.py        # Playwright-based price scraper
‚îú‚îÄ‚îÄ storage.py        # CSV read/write logic
‚îú‚îÄ‚îÄ tracker.py        # Main orchestrator + scheduler
‚îÇ
‚îú‚îÄ‚îÄ data/
‚îÇ   ‚îî‚îÄ‚îÄ prices.csv    # Price history (auto-generated)
‚îÇ
‚îú‚îÄ‚îÄ requirements.txt
‚îî‚îÄ‚îÄ README.md
```

---

## Ì∫Ä Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/price-tracker.git
cd price-tracker
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Configure your settings

Edit `config.py` with your own values:

```python
TELEGRAM_TOKEN = "your_bot_token"      # From @BotFather on Telegram
TELEGRAM_CHAT_ID = "your_chat_id"      # From @userinfobot on Telegram

PRODUCTS = [
    {
        "name": "Gigabyte RTX 5080 Wind",
        "url": "https://www.cdiscount.com/...",
        "target_price": 1200            # Alert if price drops below this
    }
]
```

### 4. Run the tracker
```bash
python tracker.py
```

---

## ‚öôÔ∏è How It Works

1. **Scraper** opens a real Chromium browser via Playwright and navigates to the product page
2. **Price extraction** finds and cleans the price from the HTML (e.g. `1 549,99 ‚Ç¨` ‚Üí `1549.99`)
3. **Comparison** checks the current price against the last recorded price in the CSV
4. **Alert** sends a Telegram message if the price dropped or hit the target threshold
5. **Storage** saves the new price with a timestamp to the CSV for future comparisons
6. **Scheduler** repeats this process every day at 8:00 AM automatically

---

## Ì≥¶ Requirements

```
playwright
requests
schedule
```

---

## Ì¥ß Add More Products

Simply add entries to the `PRODUCTS` list in `config.py`:

```python
PRODUCTS = [
    {
        "name": "RTX 5080",
        "url": "https://www.cdiscount.com/...",
        "target_price": 1200
    },
    {
        "name": "PS5 Pro",
        "url": "https://www.cdiscount.com/...",
        "target_price": 600
    }
]
```

---

## Ì≥Ñ License

MIT License ‚Äî free to use and modify.

