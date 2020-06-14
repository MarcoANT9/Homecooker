from models import storage
from models.user import User
from models.recipe import Recipe
from models.review import Review
from os import environ, getenv
from flask import Flask, request, render_template, redirect, url_for, session
from flask_mysqldb import MySQL
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def index():
    recipes_list = []
    recipes = "nombre receta"
    description = "Breve descripcion de la receta"
    user = ["Fulanito", "Mario", "Joaquin", "Luz"]
    return render_template('index.html', recipes=recipes,
                            description=description,
                            user=user)

@app.route('/recipes')
def recipes():
    response = requests.get(url="http://127.0.0.1:5000/api/v1/recipes/")
    params = response.json()
    print(params)
    return render_template('recipes.html', params=params)

if __name__ == '__main__':
    if getenv('HMCR_API_HOST'):
        app.run(host=getenv('HMCR_API_HOST'),
                port=getenv('HMCR_API_PORT'), threaded=True, debug=True)
    else:
        app.run(host='0.0.0.0', threaded=True, debug=True)
