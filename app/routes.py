from flask import Blueprint, render_template
from app.services.worldbank_api import get_gdp_data, get_population_data

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
def dashboard():
    gdp_years, gdp_values = get_gdp_data()
    population_years, population_values = get_population_data()
    return render_template('dashboard.html', gdp_years=gdp_years, gdp_values=gdp_values, population_years=population_years, population_values=population_values)
