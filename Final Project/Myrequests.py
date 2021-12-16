
from urllib import request, parse
import json

from objects import Category, Meal

# Get a list of the sent categories
def get_categories():
    url= "https://www.themealdb.com/api/json/v1/1/list.php?c=list"
    f= request.urlopen(url)
    categories = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for category_data in data['meals']:
            category = Category(category_data['strCategory'])

            categories.append(category)
    
    except (ValueError, KeyError, TypeError):
        return None

    return categories

# Get a the meal by category
def get_meals_by_category(category):
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + category
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            meal = Meal(meal_data['idMeal'],
            meal_data['strMeal'],
            meal_data['strMealThumb'])

            meals.append(meal)
    
    except (ValueError, KeyError, TypeError):
        return None

    return meals

def get_meal_by_name(meal):
    url = "www.themealdb.com/api/json/v1/1/search.php?s=" + meal
    f = request.urlopen(url)

    try:
        data = json.loads(f.read().decode('utf-8'))
        
    
    except (ValueError, KeyError, TypeError):
        return None

    return meal