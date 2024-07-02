from flask import Blueprint, render_template
from app.services.worldbank_api import get_gdp_data, get_population_data

main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    gdp_years, us_gdp_values, de_gdp_values = get_gdp_data()
    population_years, us_population_values, de_population_values = get_population_data()
    return render_template('dashboard.html', 
                           gdp_years=gdp_years, us_gdp_values=us_gdp_values, de_gdp_values=de_gdp_values, 
                           population_years=population_years, us_population_values=us_population_values, de_population_values=de_population_values)
