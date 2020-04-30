import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Client, Product, database_path

unittest.TestLoader.sortTestMethodsUsing = None

"""Active tokens for RBAC"""
auth_header_admin = {
    'Authorization': ('Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtp' +
                      'ZCI6IkdaOGJ6anR4RVpyQ2gwY0V2OHJuVCJ9.eyJpc3MiOi' +
                      'JodHRwczovL25pY2guZXUuYXV0aDAuY29tLyIsInN1YiI6I' +
                      'mF1dGgwfDVlYTdhZWRkY2YxOTBmMGMwZjZlNDBkNCIsImF1' +
                      'ZCI6ImNhcHN0b25lIiwiaWF0IjoxNTg4MjM2NDgxLCJleHA' +
                      'iOjE1ODgzMjI4ODEsImF6cCI6IkdSaHRWSk9KZm5aQjZZMm' +
                      'RMUnhWdERzR05IOElMS3pIIiwic2NvcGUiOiIiLCJwZXJta' +
                      'XNzaW9ucyI6WyJkZWxldGU6Y2xpZW50cyIsImRlbGV0ZTpw' +
                      'cm9kdWN0cyIsImdldDpjbGllbnRzIiwiZ2V0OnByb2R1Y3R' +
                      'zIiwicGF0Y2g6Y2xpZW50cyIsInBhdGNoOnByb2R1Y3RzIi' +
                      'wicG9zdDpjbGllbnRzIiwicG9zdDpwcm9kdWN0cyJdfQ.Ck' +
                      'Ncmci1zBUfGepaHva-q8n1jEa7EOJmv4n4CArwEk1EKIk_t' +
                      'yZCBuC7380Id2vIvoGi05909L9UqCBk6RSybJNh4IxjxCt-' +
                      'M6ByPpHTaeKpGXX3qeWhtrm7c7RiK_35gF6RgdvFQh50nlW' +
                      'b2BtrvnZYzZr-qqcmoUvpN5keVHqWVecfocxjrNZqL7MQZb' +
                      'VDL6sqbIHa7_F-FEyQ2J7ufX0zOG4-QXJLFno92AI20TxWp' +
                      '69VeSPwhUk5kgsOgBuDS9X7OUvQWo07nrpq7ZlbsvNCaX9J' +
                      '24w9BLPim18edbOQvGGHS6Z7ctjOCYjCocNrsjsYQv57i8D' +
                      'uF-6NrGoneQ')
}

auth_header_client = {
    'Authorization': ('Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtp' +
                      'ZCI6IkdaOGJ6anR4RVpyQ2gwY0V2OHJuVCJ9.eyJpc3MiOi' +
                      'JodHRwczovL25pY2guZXUuYXV0aDAuY29tLyIsInN1YiI6I' +
                      'mF1dGgwfDVlYTdhZDY1NmM4ZWIyMGMxNTM0OWUxZCIsImF1' +
                      'ZCI6ImNhcHN0b25lIiwiaWF0IjoxNTg4MjM2NTgxLCJleHA' +
                      'iOjE1ODgzMjI5ODEsImF6cCI6IkdSaHRWSk9KZm5aQjZZMm' +
                      'RMUnhWdERzR05IOElMS3pIIiwic2NvcGUiOiIiLCJwZXJta' +
                      'XNzaW9ucyI6WyJkZWxldGU6Y2xpZW50cyIsImdldDpwcm9k' +
                      'dWN0cyIsInBhdGNoOmNsaWVudHMiLCJwb3N0OmNsaWVudHM' +
                      'iXX0.oXY9NJL-2Qh4VYMN4r7jCvjqhzs9YVcQrVtfBj6wcP' +
                      'OOHgQmdMkEck4e_s96I9X2ACWNWdujfXEQTA6jB8YmFwJeV' +
                      '54KyfrMCEE8T-J6GLVxd_0wJ_PlFskP23Px3E0569lo-L6K' +
                      '8TKjVikY43m72W05yk6OKmq1c7tXjaCOU6adRvhH1CEuPGn' +
                      'rn4HJoxkC2byLcuqSLEIgEykQYsgJ-GyjrAPHh_wwEGKnFU' +
                      '8FBkm-xJaXSy8YZZlLPNSj_aI-MLj0bebwDSaDSYRBi96NF' +
                      'R7gzI7xgc-Nv0Rht8AOoO6LMf7BmuybAHhHEoSesOJxJaaC' +
                      'xs818z-kk8dfegK1UA')
}

new_client_id = 1
new_product_id = 13


class CapstoneTestCase(unittest.TestCase):
    """
    This class represents the test cases
    of resources of the FSND Capstone project
    """

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = ('postgres://qmmltywmjdalzd:11548019713a5731' +
                              'a52d7f5deeb74f171f19618c3bd6c846e0f37d2ee2' +
                              'a36a1a@ec2-52-7-39-178.compute-1.amazonaws' +
                              '.com:5432/d9ii0qpm1m15jp')
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
            "id_number": "1962143319087",
            "email": "indiana.jones@mcs.com",
            "phone": "0804613178"
        }

        self.new_product = {
            "name": "Macaroni",
            "description": "Pasta type of product",
            "price": 99.99
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
        """
        Test for the creation of a product with the
        /products endpoint with an authorised user
        """
        res = self.client().post('/products', headers=auth_header_admin,
                                 json=self.new_product)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['product'])

    def test_create_new_product_unauthorized(self):
        """
        Test for the creation of a new product with the
        /products endpoint with an unauthorised user
        """
        res = self.client().post('/products', headers=auth_header_client,
                                 json=self.new_product)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorised')
        self.assertEqual(data['description'], 'Required permission not found.')

    def test_get_products(self):
        """
        Test for the "GET /products endpoint handler
        """
        res = self.client().get('/products')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['products']))
        self.assertTrue(data['total products'])

    def test_remove_product(self):
        """
        Test for the DELETE /products endpoint handler where a
        specific productis to be deleted
        """
        res = self.client().delete('/products/{}'.format(new_product_id),
                                   headers=auth_header_admin)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_remove_product_error422(self):
        """
        Test for the DELETE /questions endpoint handler where a
        specific product is not available in the database
        """
        res = self.client().delete('/products/{}'.format(new_product_id),
                                   headers=auth_header_admin)
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
        """
        Test for the creation of a new client with the
        /clients endpoint
        """
        res = self.client().post('/clients', headers=auth_header_client,
                                 json=self.new_client)
        data = json.loads(res.data)
        global new_client_id
        new_client_id = int(data['client']['id'])
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['client'])

    def test_create_new_client_unauthorized(self):
        """
        Test for the creation of a product with
        an unauthorised user
        """
        res = self.client().post('/clients', json=self.new_client)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['code'], 'unauthorised')
        self.assertEqual(data['description'],
                         'No authorisation header - Not authorised')

    def test_get_clients(self):
        """Test for the "GET /clients endpoint handler"""
        res = self.client().get('/clients', headers=auth_header_admin,
                                json=self.new_client)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['clients']))
        self.assertTrue(data['total clients'])

    def test_patch_client(self):
        """
        Test for the updating of a CLIENT record
        on the /clients endpoint
        """
        new_id_num = {
            "id_number": "2004270179087"
        }
        res = self.client().patch('/clients/{}'.format(new_client_id),
                                  headers=auth_header_admin,
                                  json=new_id_num)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['client'])

    def test_404_patch_client_no_info(self):
        """
        Test for the updating of a CLIENT record on
        the /clients endpoint
        """
        res = self.client().patch('/clients/{}'.format(new_client_id),
                                  headers=auth_header_admin)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    def test_remove_client(self):
        """
        Test for the DELETE /clients endpoint handler where a
        specific client is to be deleted"""
        res = self.client().delete('/clients/{}'.format(new_client_id),
                                   headers=auth_header_admin)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    def test_404_remove_client(self):
        """
        Test for the DELETE /questions endpoint handler where a
        specific question is to be deleted
        """
        res = self.client().delete('/questions/{}'.format(new_client_id),
                                   headers=auth_header_admin)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
