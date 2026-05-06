from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv

### API key for the tiingo
load_dotenv()
api_key = os.getenv('key')
print("API KEY:", api_key)

# Create your views here.
def home(request) : 

    data = []  # ✅ instead of None
    ticker = request.GET.get('ticker')

    if ticker:
        url = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices"

        headers = {
            "Content-Type": "application/json"
        }

        params = {
            "token": api_key
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            json_data = response.json()

            last_30 = json_data[-30:]

            data = [
                {
                    "date": item["date"][:10],
                    "open": item["open"],
                    "high": item["high"],
                    "low": item["low"],
                    "close": item["close"],
                }
                for item in last_30
            ]
        else:
            print("API failed:", response.status_code)

        print("Ticker:", ticker)
        print("Data length:", len(data))
        print("Sample data:", data[:2])

    return render(request, "core/home.html", {"data": data})