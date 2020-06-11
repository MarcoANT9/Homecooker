#!/usr/bin/python3
from models.review import Review
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/recipes/<recipe_id>/reviews', strict_slashes=False)
def get_reviews(recipe_id=None):
    """
    Takes a recipe id and queries storage for the reviews of that recipe

    Args:
        recipe_id: id of recipe to search it's reviews

    Returns:
        list of reviews for the recipe in json format
    """

    recipe = storage.get(Recipe, recipe_id)
    print(recipe)
    if not recipe:
        abort(404)
    reviews = []
    for review in recipe.reviews:
        reviews.append(review.to_dict())
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', strict_slashes=False)
def get_review(review_id=None):
    """
    Takes an id and queries storage for a review that matches it

    Args:
        review_id: id of review to find

    Returns:
        review data in json format
    """

    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/del_review/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_review(review_id=None):
    """
    Takes an id and if a review with that id is found deletes it

    Args:
        review_id: id of review to delete

    Returns:
        empty json with status code 200
    """

    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    review.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/recipes/<recipe_id>/new_review', methods=['POST'],
                 strict_slashes=False)
def post_review(recipe_id=None):
    """
    Takes an id and queries storgae for a recipe with that id,
    if found creates a review with the info recieve in the body of the request

    Args:
        recipe_id: recipe that review must be part of

    Returns:
        The data of the new review with status code 201
    """

    if not storage.get(Recipe, recipe_id):
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'user_id' not in data.keys():
        abort(400, 'Missing user_id')
    if not storage.get(User, data['user_id']):
        abort(404)
    if 'text' not in data.keys():
        abort(400, 'Missing text')
    data['recipe_id'] = recipe_id
    new_review = Review(**data)
    storage.new(new_review)
    storage.save()
    return make_response(jsonify(new_review.to_dict()), 201)


@app_views.route('/update_review/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def put_review(review_id=None):
    """
        Takes an id, queries the storage for a review with that id,
        if found, updates it with the info in the body

        Args:
            review_id: id of the review to update

        Returns:
            The data of the updated review with status code 200
    """

    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    keys_ignore = ['id', 'user_id', 'recipe_id', 'created_at', 'updated_at']
    for key in data.keys():
        if key not in keys_ignore:
            setattr(review, key, data[key])
    review.save()
    return make_response(jsonify(review.to_dict()), 200)
