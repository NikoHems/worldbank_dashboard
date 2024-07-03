import requests

def fetch_worldbank_data(indicator, country, start_year, end_year):
    url = f"http://api.worldbank.org/v2/country/{country}/indicator/{indicator}?date={start_year}:{end_year}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data and len(data) > 1:
            return data[1]  # The actual data is in the second element of the returned list
    return None

def get_gdp_data():
    us_data = fetch_worldbank_data('NY.GDP.MKTP.CD', 'US', 2011, 2021)
    de_data = fetch_worldbank_data('NY.GDP.MKTP.CD', 'DE', 2011, 2021)
    if us_data and de_data:
        years = [item['date'] for item in us_data if item['value'] is not None]
        us_values = [item['value'] for item in us_data if item['value'] is not None]
        de_values = [item['value'] for item in de_data if item['value'] is not None]
        return years, us_values, de_values
    return [], [], []

def get_population_data():
    us_data = fetch_worldbank_data('SP.POP.TOTL', 'US', 2011, 2021)
    de_data = fetch_worldbank_data('SP.POP.TOTL', 'DE', 2011, 2021)
    if us_data and de_data:
        years = [item['date'] for item in us_data if item['value'] is not None]
        us_values = [item['value'] for item in us_data if item['value'] is not None]
        de_values = [item['value'] for item in de_data if item['value'] is not None]
        return years, us_values, de_values
    return [], [], []

def get_interesting_numbers():
    indicators = {
        'GDP Growth (%)': 'NY.GDP.MKTP.KD.ZG',
        'Life Expectancy': 'SP.DYN.LE00.IN',
        'Unemployment (%)': 'SL.UEM.TOTL.ZS',
        'Internet Users (%)': 'IT.NET.USER.ZS'
    }
    interesting_numbers = {}
    for name, indicator in indicators.items():
        us_data = fetch_worldbank_data(indicator, 'US', 2021, 2021)
        de_data = fetch_worldbank_data(indicator, 'DE', 2021, 2021)
        print(f"Indicator: {name}, US Data: {us_data}, DE Data: {de_data}")  # Debugging print
        interesting_numbers[name] = {
            'US': round(us_data[0]['value'], 2) if us_data and us_data[0]['value'] is not None else 'N/A',
            'DE': round(de_data[0]['value'], 2) if de_data and de_data[0]['value'] is not None else 'N/A'
        }
    print(f"Interesting Numbers: {interesting_numbers}")  # Debugging print
    return interesting_numbers
