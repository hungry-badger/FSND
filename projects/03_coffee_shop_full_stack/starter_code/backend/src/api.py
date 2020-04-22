import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
# db_drop_and_create_all()

'''ROUTES'''


@app.route('/')
@requires_auth
def hello_world():
    jwt = get_token_auth_header()
    print(jwt)
    return jsonify(jwt)


'''
GET /drinks endpoint
    Public endpoint.
    Contains only the drink.short() data representation.
    Returns status code 200 and json {"success": True, "drinks": drinks} \
        where drinks is the list of drinks. Otherwise returns appropriate \
            status code indicating reason for failure.
'''


@app.route('/drinks', methods=['GET'])
def get_drinks():
    try:
        drinks = Drink.query.all()
        short_drinks = [d.short() for d in drinks]
    except:
        raise AuthError({
            'code': 'no_data',
            'description': 'Unable to find any drinks.'
        }, 404)

    return jsonify({
        'success': True,
        'status_code': 200,
        'drinks': short_drinks
    })


'''
GET /drinks-detail endpoint
    Require the 'get:drinks-detail' permission
    Contain the drink.long() data representation
    Returns status code 200 and json {"success": True, "drinks": drinks} \
        where drinks is the list of drinks \
            or appropriate status code indicating reason for failure
'''


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(payload):
    try:
        drinks = Drink.query.all()
        long_drinks = [d.long() for d in drinks]
    except:
        raise AuthError({
            'code': 'no_data',
            'description': 'Unable to find any drinks.'
        }, 404)

    return jsonify({
        'success': True,
        'status_code': 200,
        'drinks': long_drinks
    })


'''
POST /drinks endpoint
    Create a new row in the drinks table
    Require the 'post:drinks' permission
    Contain the drink.long() data representation
    Returns status code 200 and json {"success": True, "drinks": drink} \
        where drink an array containing only the newly created drink \
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def post_drink(payload):
    drink = request.get_json()
    new_drink = Drink()
    new_drink.title = drink.get('title')
    new_drink.recipe = json.dumps(drink.get('recipe'))
    new_drink.insert()

    return jsonify({
        'success': True,
        'status_code': 200,
        'drinks': new_drink.long()
    })


'''
PATCH /drinks/<id> endpoint
    <id> is the existing drink id
    Responds with a 404 error if <id> is not found
    Updates the corresponding row for <id>
    Requires the 'patch:drinks' permission
    Contains the drink.long() data representation
    Returns status code 200 and json {"success": True, "drinks": drink}\
        where drink an array containing only the updated drink\
            or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:q_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(payload, q_id):
    update_info = request.get_json()
    update_title = update_info.get('title', None)
    update_recipe = update_info.get('recipe', None)

    update_drink = Drink.query.filter(Drink.id == q_id).one_or_none()
    if not update_drink:
        return jsonify({
            'success': False,
            'status_code': 404,
            'message': 'Drink not found.'
        })

    if (update_title is None) and (update_recipe is None):
        abort(422)

    if update_title:
        update_drink.title = update_title
    if update_recipe:
        update_drink.recipe = json.dumps(update_recipe)
    update_drink.update()

    return jsonify({
        'success': True,
        'status_code': 200,
        'drinks': update_drink.long()
    })


'''
DELETE /drinks/<id> endpoint
    Where <id> is the existing drink id
    Responds with a 404 error if <id> is not found
    Deletes the corresponding row for <id>
    Require the 'delete:drinks' permission
    Returns status code 200 and json {"success": True, "delete": id}\
        where id is the id of the deleted record\
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:q_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, q_id):
    try:
        drink = Drink.query.filter(Drink.id == q_id).one_or_none()
        if drink is None:
            abort(404)

        drink.delete()

        return jsonify({
            'success': True,
            'status_code': 200,
            'delete': q_id
        })
    except:
        abort(422)


'''Error Handling'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

'''
@app.errorhandler(AuthError)
def auth_error(AuthError):
    return jsonify({
        "success": False,
        "error": AuthError.code,
        "message": AuthError.description
    }), 401
'''


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify(error.error), error.status_code

'''
----------------------------------------------------------------------------#
Launch.
----------------------------------------------------------------------------#
'''

if __name__ == '__main__':
    app.run()
