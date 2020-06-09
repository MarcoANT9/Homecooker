#!/usr/bin/python3
"""Returns json with status"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def stats():
    all_objs = {
                'reviews': storage.count('Review'),
                'recipes': storage.count('Recipe'),
                'users': storage.count('User')
                }
    return jsonify(all_objs)