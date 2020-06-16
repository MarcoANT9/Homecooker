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
    recipe = jsonify(recipes)

    users = storage.all('User')
    users_list = []
    for user in users.values():
        users_list.append(user.to_dict())
    user = jsonify(users_list)

    recipess = "recetica"
    description = "descripcioncita"
    return render_template("index.html", recipes=recipess,
                            description=description,
                            user="")

@app.route('/recipe')
def recipe():

    return render_template("recipes.html", user="")

if __name__ == '__main__':
    if getenv('HMCR_API_HOST'):
        app.run(host=getenv('HMCR_API_HOST'),
                port=getenv('HMCR_API_PORT'), threaded=True, debug=True)
    else:
        app.run(host='0.0.0.0', threaded=True, debug=True)
