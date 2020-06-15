#!/usr/bin/python3
""" Flask Application """
from api.v1.views import app_views
from models import storage
from models import user
from os import environ, getenv
from flask import Flask, render_template, make_response, jsonify
from flask import request, url_for, session
from flask_cors import CORS
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

if getenv('HMCR_TYPE_STORAGE') == "db":
    app.config['MYSQL_HOST'] = getenv('HMCR_MYSQL_HOST')
    app.config['MYSQL_USER'] = getenv('HMCR_MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = getenv('HMCR_MYSQL_PWD')
    app.config['MYSQL_DB'] = getenv('HMCR_MYSQL_DB')
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    mysql = MySQL(app)


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


@app.route('/login', methods=["GET", "POST"],
           strict_slashes=False)
def login():
    """Route for user login"""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM Users WHERE email={%s}".format(email))
        user = curl.fetchone()
        curl.close

        if len(user) > 0:
            if md5(password.encode()).hexdigest() == user["password"]:
                if user['first_name'] is None:
                    session['name'] = user['nickname']
                else:
                    session['name'] = user['first_name']

                session['email'] = user['email']
                return render_template('index.html')
            else:
                return "Error: Password and email don't match"
        else:
            return "Error: User not found"
    else:
        return render_template("login.html")  # <- Posible cambio aqui


@app.route('/logout', strict_slashes=False)
def logout():
    """Defines the logout procedure"""
    session.clear()
    return render_template("index.html")


if __name__ == '__main__':
    if getenv('HMCR_API_HOST'):
        app.run(host=getenv('HMCR_API_HOST'),
                port=getenv('HMCR_API_PORT'), threaded=True)
    else:
        app.run(host='0.0.0.0', threaded=True)
