from models import storage
from models.user import User
from models.recipe import Recipe
from models.review import Review
from os import environ, getenv
from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
import requests

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/')
def home():
    recipes = []
    all_ = storage.all(Recipe).values()
    for value in all_:
        recipes.append(value.to_dict())

    users = storage.all('User')
    users_list = []
    for user in users.values():
        users_list.append(user.to_dict())
    return render_template("index.html", recipes=recipes,
                            user=user)

@app.route('/recipe')
def recipe():
    response = requests.get(url="http://127.0.0.1:5001/api/v1/recipes")
    recipes = response.json()
    for recipe in recipes:
        recipe_dict = dict(recipe)
    print(recipe_dict)
    return render_template("recipes.html", recipes=recipe_dict)

@app.route('/recipe/<id>')
def recipe_id(id):
    all_ = storage.all(Recipe).values()
    for value in all_:
        if value.id == id:
            recipes = value.to_dict()
    print(recipes)
    return render_template("recipes.html", recipes=recipes)

if __name__ == '__main__':
    if getenv('HMCR_API_HOST'):
        app.run(host=getenv('HMCR_API_HOST'),
                port=getenv('HMCR_API_PORT'), threaded=True, debug=True)
    else:
        app.run(host='0.0.0.0', threaded=True, debug=True)
