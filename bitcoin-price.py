import requests
import sys
import io
import time
from datetime import datetime
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding="utf-8", line_buffering=True)


def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        price = data["bitcoin"]["usd"]
        return price

    except requests.exceptions.RequestException as e:
        print("خطا", e)
        return None


def track_price_live(interval_seconds=10):
    print(f"شروع پیگیری لحظه ای قیمت بیت کوین ( {interval_seconds})")
    print("برای توقف Ctrl+C .\n بزن")

    try:
        while True:
            price = get_bitcoin_price()
            current_time = datetime.now().strftime("%H:%M:%S")

            if price is not None:
                print(f"[{current_time}] قیمت بیت کوین: {price:,}دلار")
            else:
                print(f"[{current_time}] دریافت قیمت ناموفق بود.")
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("\nبرنامه متوقف شد!")


if __name__ == "__main__":
    track_price_live(interval_seconds=10)
