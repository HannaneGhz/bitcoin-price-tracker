import requests
import sys
import io
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        price = data["bitcoin"]["usd"]
        return price

    except requests.exceptions.RequestException as e:
        print("خطا", e)
        return None


if __name__ == "__main__":
    price = get_bitcoin_price()

    if price is not None:
        print(f"قیمت لحظه ای بیت کوین: {price:,} دلار")
    else:
        print("قیمت دریافت نشد")
