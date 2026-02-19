from playwright.sync_api import sync_playwright

def get_price(url: str) -> float | None:
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=False,  # mode visible pour éviter la détection
                args=["--disable-blink-features=AutomationControlled"]
            )
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
                viewport={"width": 1280, "height": 720},
                locale="fr-FR",
                extra_http_headers={
                    "Accept-Language": "fr-FR,fr;q=0.9",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                }
            )
            page = context.new_page()
            page.goto(url, wait_until="networkidle", timeout=30000)
            
            # Attendre que le prix soit chargé
            page.wait_for_selector("[data-e2e='price']", timeout=10000)
            price_el = page.query_selector("[data-e2e='price']")

            if not price_el:
                print("Prix non trouvé")
                browser.close()
                return None

            price_text = price_el.inner_text()
            price_text = price_text.replace("€", ".").replace("\xa0", "").replace(" ", "").strip()
            browser.close()
            return float(price_text)

    except Exception as e:
        print(f"Erreur : {e}")
        return None