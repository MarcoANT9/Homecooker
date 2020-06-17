import json
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
                            user="")

@app.route('/recipe')
def recipe():
    response = requests.get(url="http://127.0.0.1:5001/api/v1/recipes")
    recipes = response.json()
    for recipe in recipes:
        recipe_dict = dict(recipe)
    return render_template("recipes.html", recipes=recipe_dict)

@app.route('/recipe/<id>')
def recipe_id(id):
    all_ = storage.all(Recipe).values()
    for value in all_:
        if value.id == id:
            recipes = value.to_dict()
    return render_template("recipes.html", recipes=recipes)

@app.route('/new_user', methods=['POST'])
def new_user():
    first_name = request.form["first_name"]
    last_name=request.form["last_name"]
    nickname=request.form["nickname"]
    email=request.form["email"]
    password = request.form["password"]
    user_type = 0
    dict_user = {
        'first_name':first_name,
        'last_name':last_name,
        'nickname':nickname,
        'email':email,
        'password':password,
        'user_type':user_type
    }
    r = requests.post(url="http://0.0.0.0:5000/api/v1/new_user", json=dict_user)
    if r.status_code == 400:
        print("Usuario no creado")
    else:
        print("Usuario creado")
    return redirect("/")

@app.route('/new_chef', methods=['POST'])
def new_chef():
    first_name = request.form["first_name"]
    last_name=request.form["last_name"]
    nickname=request.form["nickname"]
    email=request.form["email"]
    password = request.form["password"]
    website = request.form["website"]
    profile_image = request.form["profile_image"]
    user_type = 1
    dict_chef = {
        'first_name':first_name,
        'last_name':last_name,
        'nickname':nickname,
        'email':email,
        'password':password,
        'website':website,
        'profile_image':profile_image,
        'user_type':user_type
    }
    r = requests.post(url="http://0.0.0.0:5000/api/v1/new_user", json=dict_chef)
    if r.status_code == 400:
        print("Usuario no creado")
    else:
        print("Usuario creado")
    return redirect("/")

@app.route('/new_recipe', methods=['POST'])
def new_recipe():
    first_name = request.form["first_name"]
    last_name=request.form["last_name"]
    nickname=request.form["nickname"]
    email=request.form["email"]
    password = request.form["password"]
    user_type = 0
    dict_user = {
        'first_name':first_name,
        'last_name':last_name,
        'nickname':nickname,
        'email':email,
        'password':password,
        'user_type':user_type
    }
    r = requests.post(url="http://0.0.0.0:5000/api/v1/new_user", json=dict_user)
    if r.status_code == 400:
        print("Receta no creada")
    else:
        print("Receta creada")
    return redirect("/")

if __name__ == '__main__':
    if getenv('HMCR_API_HOST'):
        app.run(host=getenv('HMCR_API_HOST'),
                port=getenv('HMCR_API_PORT'), threaded=True, debug=True)
    else:
        app.run(host='0.0.0.0', threaded=True, debug=True)
