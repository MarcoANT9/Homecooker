#!/usr/bin/python3
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/users', strict_slashes=False)
def get_users():
    """
    List all users in storage

    Returns:
        list of users in json format
    """

    users = storage.all('User')
    users_list = []
    for user in users.values():
        users_list.append(user.to_dict())
    return jsonify(users_list)


@app_views.route('/users/<user_id>', strict_slashes=False)
def get_user(user_id=None):
    """
    Takes an id and queries storage for a user with that id

    Args:
         user_id: id of a user to find

    Returns:
        user data in json format
    """

    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/del_user/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_user(user_id=None):
    """
    Takes the id of a user and if a user with that id is found deletes it

    Args:
        user_id: id of user to delete

    Returns:
        empty json with status code 200
    """

    user = storage.get(User, user_id)
    if not user:
        abort(404)
    user.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/create_user', methods=['POST'],
                 strict_slashes=False)
def post_user():
    """
    Creates a user with the info recieved in the body of the request

    Returns:
        The data of the new user with status code 201
    """

    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'email' not in data.keys():
        abort(400, 'Missing email')
    if 'password' not in data.keys():
        abort(400, 'Missing password')
    new_user = User(**data)
    storage.new(new_user)
    storage.save()
    return make_response(jsonify(new_user.to_dict()), 201)


@app_views.route('/update_user/<user_id>', methods=['PUT'],
                 strict_slashes=False)
def put_user(user_id=None):
    """
        Takes an id, queries the storage for a user with that id and if found,
        updates it with the info in the body of the request

        Args:
            user_id: id of the user to update

        Returns:
            The data of the updated user with status code 200
    """

    user = storage.get(User, user_id)
    if not user:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    keys_ignore = ['id', 'email', 'created_at', 'updated_at']
    for key in data.keys():
        if key not in keys_ignore:
            setattr(user, key, data[key])
    user.save()
    return make_response(jsonify(user.to_dict()), 200)  