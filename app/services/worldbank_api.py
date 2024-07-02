import requests

def fetch_worldbank_data(indicator, country, start_year, end_year):
    url = f"http://api.worldbank.org/v2/country/{country}/indicator/{indicator}?date={start_year}:{end_year}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[1]  # The actual data is in the second element of the returned list
    else:
        return None

def get_gdp_data():
    data = fetch_worldbank_data('NY.GDP.MKTP.CD', 'US', 2011, 2021)
    if data:
        years = [item['date'] for item in data]
        values = [item['value'] for item in data]
        return years, values
    return [], []

def get_population_data():
    data = fetch_worldbank_data('SP.POP.TOTL', 'US', 2011, 2021)
    if data:
        years = [item['date'] for item in data]
        values = [item['value'] for item in data]
        return years, values
    return [], []
