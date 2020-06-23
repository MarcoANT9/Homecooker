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

""" homepage endpoint """
@app.route('/')
def home():
    """
        get recipes and users from the database
    """
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

""" recipe without id """
@app.route('/recipe')
def recipe():
    """
        get recipes from the api´s function with requests method
    """
    response = requests.get(url="http://127.0.0.1:5001/api/v1/recipes")
    recipes = response.json()
    for recipe in recipes:
        recipe_dict = dict(recipe)
    return render_template("recipes.html", recipes=recipe_dict)

""" endpoint recipe with id """
@app.route('/recipe/<id>')
def recipe_id(id):
    """
        get recipe by id from the database
    """
    all_ = storage.all(Recipe).values()
    for value in all_:
        if value.id == id:
            recipes = value.to_dict()
    return render_template("recipes.html", recipes=recipes)

""" endpoint to create new common user """
@app.route('/new_user', methods=['POST'])
def new_user():
    """
        get data from form and do post request to add this to database
    """
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

""" endpoint to create new chef user """
@app.route('/new_chef', methods=['POST'])
def new_chef():
    """
        get data from form and do post request to add this to database
    """
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

""" endpoint to create new recipe """
@app.route('/new_recipe', methods=['POST'])
def new_recipe():
    """
        get data from form and do post request to add this to database
    """
    name = request.form["name"]
    description=request.form["description"]
    ingredients=request.form["ingredients"]
    preparation=request.form["preparation"]
    video_url = request.form["video_url"]
    recipe_img = request.form["recipe_img"]
    dict_recipe = {
        'name':name,
        'description':description,
        'ingredients':ingredients,
        'preparation':preparation,
        'video_url':video_url,
        'recipe_img':recipe_img
        }
    r = requests.post(url="http://0.0.0.0:5000/api/v1/new_user", json=dict_recipe)
    if r.status_code == 400:
        print("Receta no creada")
    else:
        print("Receta creada")
    return redirect("/recipe/<id>")

if __name__ == '__main__':
    if getenv('HMCR_API_HOST'):
        app.run(host=getenv('HMCR_API_HOST'),
                port=getenv('HMCR_API_PORT'), threaded=True, debug=True)
    else:
        app.run(host='0.0.0.0', threaded=True, debug=True)
