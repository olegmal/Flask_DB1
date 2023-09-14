from flask import Flask, jsonify, render_template, request
import os
import sqlite3


DATABASE = '///store_db.sqlite'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'store_db.sqlite')))

# def main():
#     app = Flask(__name__)
#     app.config["DEBUG"] = True
#
def db_connect(query):
    connection = sqlite3.connect('store_db.sqlite')
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result


@app.route('/names/')
def unique_names():
    query = f"""
        SELECT DISTINCT first_name
        FROM customers;
        """

    response = db_connect(query)
    response_json = {
        'first_name': response,
    }
    return jsonify(response_json)


@app.route('/customers/<id>')
def customers(id):
    query = f"""
        SELECT first_name, last_name
        FROM customers
        WHERE id = {id};
        """
    response = db_connect(query)[0]
    response_json = {
        'first_name': response[0],
        'last_name': response[1]
    }
    return jsonify(response_json)


@app.route('/count/')
def count_tracks():
    query = f"""
        SELECT COUNT(id)
        FROM tracks;
        """
    response = db_connect(query)
    response_json = {
        "id" : response[0]
    }
    return jsonify(response_json)


@app.route('/tracks/')
def track_duration():
    query = f"""
        SELECT name, duration
        FROM tracks;
        """
    response = db_connect(query)
    response_json = {
        'duration': response
    }
    return jsonify(response_json)


if __name__ == '__main__':
    app.run(debug=True)
