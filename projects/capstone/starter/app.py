import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Client, Product, Sales

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS is enabled for specific request types as per below
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, DELETE, OPTIONS')
        return response


    @app.route('/')
    def get_greeting():
        greeting = "Welcome to the JUNGLE!!!"
        return greeting


    @app.route('/clients', methods = ['GET'])
    def get_clients():
        try:
            clients = Client.query.all()
            all_clients = []
            for c in clients:
                all_clients.append({
                    'id': c.id, 
                    'first_name': c.first_name,
                    'surname': c.surname,
                    'id_number': c.id_number,
                    'email': c.email,
                    'phone': c.phone
                })
        
        except:
            abort(404)
        
        return jsonify({
            'success': True,
            'status_code': 200,
            'clients': all_clients,
            'total clients': len(clients)
        })


    @app.route('/clients', methods = ['POST'])
    def create_clients():
        info = request.get_json()
        new_first_name = info.get('first_name', None)
        new_surname = info.get('surname', None)
        new_id_number = info.get('id_number', None)
        new_email = info.get('email', None)
        new_phone = info.get('phone', None)

        if (new_first_name is None) or (new_surname is None) \
            or (new_id_number is None) or (new_email is None) \
                or (new_phone is None):
            return jsonify({
                'success': False,
                'status_code': 404,
                'message': 'All client fields required'
            })

        try:
            new_client = Client(first_name = new_first_name, 
                                surname = new_surname,
                                id_number = new_id_number,
                                email = new_email, phone = new_phone)
            new_client.insert()
            return jsonify({
                'success': True,
                'status_code': 200,
                'client': new_client
            })
        except:
            abort(422)


        clients = Client.query.all()
        all_clients = {}
        for c in clients:
            all_clients[c.id] = c.id 
            all_clients[c.first_name] = c.first_name
            all_clients[c.surname] = c.surname
            all_clients[c.id_number] = c.id_number
            all_clients[c.email] = c.email
            all_clients[c.phone] = c.phone

        return jsonify({
            'success': True,
            'status_code': 200,
            'clients': all_clients,
            'total clients': len(clients)
        })

    
    @app.route('/clients/<int:client_id>', methods = ['PATCH'])
    def update_client(client_id):
        update_client = Client.query.filter(Client.id == client_id).one_or_none()
        if not update_client:
            abort(404)
        
        update = request.get_json()
        if update is None:
            return jsonify({
                'success': False,
                'status_code': 404,
                'message': 'No update information provided'
            })
        
        updated_first_name = update.get('first_name', None)
        updated_surname = update.get('surname', None)
        updated_id_number = update.get('id_number', None)
        updated_email = update.get('email', None)
        updated_phone = update.get('phone', None)

        if updated_first_name:
            update_client.first_name = updated_first_name
        if updated_surname:
            update_client.surname = updated_surname
        if updated_id_number:
            update_client.id_number = updated_id_number
        if updated_email:
            update_client.email = updated_email
        if updated_phone:
            update_client.phone = updated_phone

        if updated_first_name or updated_surname or updated_id_number\
            or updated_email or updated_phone:
            update_client.update()
            return jsonify({
                'success': True,
                'status_code': 200,
                'client': update_client.format()
            })

        else: 
            abort(404)

    
    @app.route('/clients/<int:client_id>', methods = ['DELETE'])
    def delete_client(client_id):
        try:
            client = Client.query.filter(Client.id == client_id).one_or_none()
            if client is None:
                abort(404)
            
            client.delete()
            
            return jsonify({
                'success': True,
                'status_code': True,
                'delete': client.format()
            })
        except:
            abort(422)
    
    
    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    '''
    Error handling
    '''


    @app.errorhandler(400)
    def not_found(error):
        return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource not found"
        }), 404

    @app.errorhandler(405)
    def not_found(error):
        return jsonify({
        "success": False,
        "error": 405,
        "message": "Method not found"
        }), 405
    
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Not processable"
        }), 422

    #@app.errorhandler(AuthError)
    #def auth_error(error):
    #    return jsonify(error.error), error.status_code
    
    return app


app = create_app()

if __name__ == '__main__':
    app.run()