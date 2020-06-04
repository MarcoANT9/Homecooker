#!/usr/bin/python3
from models.user import User
from models import storage

from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from