import requests

def fetch_worldbank_data(indicator, country, start, end):
    url = f"http://api.worldbank.org/v2/country/{country}/indicator/{indicator}?date={start}:{end}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
