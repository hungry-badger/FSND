import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Client, Product, database_path

unittest.TestLoader.sortTestMethodsUsing = None

auth_header_admin = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdaOGJ6anR4RVpyQ2gwY0V2OHJuVCJ9.eyJpc3MiOiJodHRwczovL25pY2guZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTdhZWRkY2YxOTBmMGMwZjZlNDBkNCIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNTg4MTM1MzEyLCJleHAiOjE1ODgyMjE3MTIsImF6cCI6IkdSaHRWSk9KZm5aQjZZMmRMUnhWdERzR05IOElMS3pIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y2xpZW50cyIsImRlbGV0ZTpwcm9kdWN0cyIsImdldDpjbGllbnRzIiwiZ2V0OnByb2R1Y3RzIiwicGF0Y2g6Y2xpZW50cyIsInBhdGNoOnByb2R1Y3RzIiwicG9zdDpjbGllbnRzIiwicG9zdDpwcm9kdWN0cyJdfQ.g4x49OrnAC3OYvfvzewdPP-mZ-8mTmaFPkB-LLpY7Htv-ebjZ7yye4EemBi0OWqRklTb5gn1CYyv-SYvYJEEdpLnucyy0mWKBWJWVhJw2iBbUCsFSbd204doLdlK4cTBVV4j2w8uBV4G__8JX90i1dh_v0NfQUwppV9ac8b76eAOpJxcqIKNNFzDccJbQZ2sKa398Ce9JwANieqeRKNeJQjfE-2C7WDG7DC3PY1OH3fjY7Wtov4JFi7Ze1luBMWJuB1ZpLKHDDVmbV9OzzsQvmv5ABpb88V3OGMthaVNT6U5TpSiB8g0ZJ0FzdhAXZ_sqnonrg5ZY7tZQd1I2dMUjQ'
}

auth_header_client = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdaOGJ6anR4RVpyQ2gwY0V2OHJuVCJ9.eyJpc3MiOiJodHRwczovL25pY2guZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTdhZDY1NmM4ZWIyMGMxNTM0OWUxZCIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNTg4MTM1NDE1LCJleHAiOjE1ODgyMjE4MTUsImF6cCI6IkdSaHRWSk9KZm5aQjZZMmRMUnhWdERzR05IOElMS3pIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y2xpZW50cyIsImdldDpwcm9kdWN0cyIsInBhdGNoOmNsaWVudHMiLCJwb3N0OmNsaWVudHMiXX0.JpUxcaIA79xIAuINKeHrnfn_Y2qdVIrOnITmZ3mREEl0Y0fXXiju3EvcuHhXlhUJQjW-55G_TNHZ1vj6MIWJxuiFd_zwJHkoMo50rOH0nbhgLDLnVZ48L5_BTV0P6ARqZ78r-aNap-ryD72b4A7mPugeitZcVGCOF6hDuOxrLk8JZQBE7QDS4GU7TdDSrcpAT6dUCqaS8XtyPSKEsWZU9ruuJUbEDtc_oMnjvfr8UXppX9wzL_lFcB58tTrJk1TcWc2Nd39v0M-7QTwAqDc82LPN9batYcHXLY0bNjmzxMULTs4UJkvwObp3zMrG-Fx0gZr6hsKc5XN6Voxddo0aBQ'
}

new_client_id = 1
new_product_id = 84

class CapstoneTestCase(unittest.TestCase):
    """This class represents the test case of resources on the Capstone project"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capdb"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_client = {
            "first_name": "Indiana",
            "surname": "Jones",
            "id_number": "1960133319087",
            "email": "indiana.jones@mcs.com",
            "phone": "0804613178"
        }

        self.new_product = {
            "name": "Project finance",
            "description": "A project financed loan to the client",
            "price": 12.40
        }
    

    def tearDown(self):
        """Executed after reach test"""
        pass

    '''
    Removed as the database is populated
    def test_404_get_products(self):
        """Test for the "GET /products endpoint handler"""
        res = self.client().get('/products')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource not found')
    '''
    
    def test_create_new_product(self):
        """Test for the creation of a product with the """
        res = self.client().post('/products', headers=auth_header_admin, json=self.new_product)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['product'])

    
    def test_create_new_product_unauthorized(self):
        """Test for the creation of a new product with the /products endpoint"""
        res = self.client().post('/products', headers=auth_header_client, json=self.new_product)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorised')
        self.assertEqual(data['description'], 'Required permission not found.')
    

    def test_get_products(self):
        """Test for the "GET /products endpoint handler"""
        res = self.client().get('/products')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['products']))
        self.assertTrue(data['total products'])
    
    
    def test_remove_product(self):
        """Test for the DELETE /products endpoint handler where a \
        specific productis to be deleted"""
        res = self.client().delete('/products/{}'.format(new_product_id), headers=auth_header_admin)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    
    def test_remove_product_error422(self):
        """Test for the DELETE /questions endpoint handler where a 
        specific product is not available in the database"""
        res = self.client().delete('/products/{}'.format(new_product_id), headers=auth_header_admin)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    
    '''
    Test removed as the database is populated
    def test_404_get_clients(self):
        """Test for the "GET /clients endpoint handler"""
        res = self.client().get('/clients')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource not found')
    '''
    
    def test_create_new_client(self):
        """Test for the creation of a new client with the /clients endpoint """
        res = self.client().post('/clients', headers=auth_header_client, json=self.new_client)
        data = json.loads(res.data)
        global new_client_id 
        new_client_id = int(data['client']['id']) 
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['client'])



    def test_create_new_client_unauthorized(self):
        """Test for the creation of a product with the """
        res = self.client().post('/clients', json=self.new_client)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['code'], 'unauthorised')
        self.assertEqual(data['description'], 'No authorisation header - Not authorised')
    

    def test_get_clients(self):
        """Test for the "GET /clients endpoint handler"""
        res = self.client().get('/clients', headers=auth_header_admin, json=self.new_client)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['clients']))
        self.assertTrue(data['total clients'])


    def test_patch_client(self):
        """Test for the updating of a CLIENT record on the /clients endpoint """
        new_id_num = {
            "id_number": "2004270179087"
        }        
        res = self.client().patch('/clients/{}'.format(new_client_id), headers=auth_header_admin, json=new_id_num)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['client']) 

    
    def test_404_patch_client_no_info(self):
        """Test for the updating of a CLIENT record on the /clients endpoint """      
        res = self.client().patch('/clients/{}'.format(new_client_id), headers=auth_header_admin)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found') 


    def test_remove_client(self):
        """Test for the DELETE /clients endpoint handler where a 
        specific client is to be deleted"""
        res = self.client().delete('/clients/{}'.format(new_client_id), headers=auth_header_admin)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])


    def test_404_remove_client(self):
        """Test for the DELETE /questions endpoint handler where a 
        specific question is to be deleted"""
        res = self.client().delete('/questions/{}'.format(new_client_id), headers=auth_header_admin)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')   


'''
    def test_play_quiz(self):
        self.new_quiz = {'previous_questions': [],
                          'quiz_category': {'type': 'Science', 'id': 1}}

        res = self.client().post('/quizzes', json=self.new_quiz)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_422_create_question_fail(self):
        self.new_question = {
            'answer': 'Answer',
            'category': 1
        }
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        print(data)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not processable")

    def test_get_questions_from_categories(self):
        """Test for the "GET /categories/<cat_id>/questions endpoint handler"""
        c_id = 3
        res = self.client().get('/categories/{}/questions'.format(c_id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertEqual(data['current_category'], c_id)

    def test_search_question(self):
        search_term = {
            'searchTerm': 'where',
        } 

        res = self.client().post('/questions', json = search_term)
        data = json.loads(res.data)
    
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])


    def test_404_sent_beyond_valid_page(self):
        res = self.client().get('/questions\?page=3000')
        data = json.loads(res.data)
    
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_search_not_found(self):
        search_term = {
            'searchTerm': 'is there a word such as atdhikl',
        } 

        res = self.client().post('/questions', json = search_term)
        data = json.loads(res.data)
    
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_422_question_does_not_exist(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)
    
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not processable")

    def test_404_play_quiz(self):
        new_quiz = {'previous_questions': []}
        res = self.client().post('/quizzes', json=new_quiz)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not processable")
'''

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()