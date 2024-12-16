import requests

API_KEY = "Your API Key"
BASE_URL = "https://newsapi.org/v2/top-headlines"


def fetch_news(country="in", category=None, query=None):
    params = {
        "apiKey": API_KEY,
        "country": country,
        "category": category,
        "q": query,
        "pageSize": 100
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("articles", [])
    else:
        print(f"Error fetching news: {response.status_code}")
        return []
