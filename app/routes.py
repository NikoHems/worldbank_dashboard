from flask import Blueprint, render_template
from app.services.worldbank_api import fetch_worldbank_data

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
def dashboard():
    indicator = 'NY.GDP.MKTP.CD'  # Example indicator
    country = 'US'
    start = 2000
    end = 2020

    data = fetch_worldbank_data(indicator, country, start, end)

    # Extract interesting numbers
    interesting_numbers = {
        'number1': data[1][0]['value'],
        'number2': data[1][1]['value'],
        'number3': data[1][2]['value'],
        'number4': data[1][3]['value'],
    }

    return render_template('dashboard.html', data=data, interesting_numbers=interesting_numbers)
