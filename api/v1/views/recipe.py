#!/usr/bin/python3
from models.recipe import Recipe
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route("/recipes", methods=['GET'], strict_slashes=False)
def get_recipes():
    """ function that gets all the recipes """
    recipes = []
    all_ = storage.all(Recipe).values()
    for value in all_:
        recipes.append(value.to_dict())
    return jsonify(recipes)


@app_views.route("/recipes/<recipe_id>", methods=['GET'], strict_slashes=False)
def recipe_by_id(recipe_id):
    """ function that get a recipe by his id """
    recipe = storage.get("Recipe", recipe_id)
    if recipe:
        return jsonify(recipe.to_dict())
    abort(404)


@app_views.route("/recipes/<recipe_id>", methods=['DELETE'],
                 strict_slashes=False)
def del_recipe(recipe_id):
    """ function that deletes a recipe by his id """
    recipe = storage.get("Recipe", recipe_id)
    if recipe:
        recipe.delete()
        storage.save()
        return make_response(jsonify({}), 200)
    abort(404)


@app_views.route("/recipes/", methods=['POST'], strict_slashes=False)
def create_recipe():
    """ function that create a new recipe """
    new_recipe = request.get_json()
    if not new_recipe:
        abort(400, "Not a JSON")

    if new_recipe:
        if "name" not in new_recipe:
            abort(400, "Missing name")
        recipe = Recipe(**new_recipe)
        storage.new(recipe)
        storage.save()
        return make_response(jsonify(recipe.to_dict()), 201)


@app_views.route("/recipes/<recipe_id>", methods=['PUT'], strict_slashes=False)
def up_recipe(recipe_id):
    """ function that update a recipe by his id """
    recipe_up = request.get_json()
    if not recipe_up:
        abort(400, "Not a JSON")

    obj_ = storage.get(Recipe, recipe_id)
    if obj_:
        ignored_attr = ["id", "created_at", "updated_at"]
        for key, value in recipe_up.items():
            if key not in ignored_attr:
                setattr(obj_, key, value)

            obj_.save()
        return make_response(jsonify(obj_.to_dict()), 200)

    abort(404)
    storage.save()
