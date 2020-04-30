import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Client, Product, database_path

unittest.TestLoader.sortTestMethodsUsing = None

auth_header_admin = {
    'Authorization': ('Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6Ikp' +
                      'XVCIsImtpZCI6IkdaOGJ6anR4RVpyQ2gwY0V2O' +
                      'HJuVCJ9.eyJpc3MiOiJodHRwczovL25pY2guZXU' +
                      'uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYT' +
                      'dhZWRkY2YxOTBmMGMwZjZlNDBkNCIsImF1ZCI6I' +
                      'mNhcHN0b25lIiwiaWF0IjoxNTg4MTM1MzEyLCJl' +
                      'eHAiOjE1ODgyMjE3MTIsImF6cCI6IkdSaHRWSk9' +
                      'KZm5aQjZZMmRMUnhWdERzR05IOElMS3pIIiwic2' +
                      'NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxld' +
                      'GU6Y2xpZW50cyIsImRlbGV0ZTpwcm9kdWN0cyIs' +
                      'ImdldDpjbGllbnRzIiwiZ2V0OnByb2R1Y3RzIiw' +
                      'icGF0Y2g6Y2xpZW50cyIsInBhdGNoOnByb2R1Y3R' +
                      'zIiwicG9zdDpjbGllbnRzIiwicG9zdDpwcm9kdWN' +
                      '0cyJdfQ.g4x49OrnAC3OYvfvzewdPP-mZ-8mTmaF' +
                      'PkB-LLpY7Htv-ebjZ7yye4EemBi0OWqRklTb5gn1' +
                      'CYyv-SYvYJEEdpLnucyy0mWKBWJWVhJw2iBbUCsFS' +
                      'bd204doLdlK4cTBVV4j2w8uBV4G__8JX90i1dh_v0' +
                      'NfQUwppV9ac8b76eAOpJxcqIKNNFzDccJbQZ2sKa39' +
                      '8Ce9JwANieqeRKNeJQjfE-2C7WDG7DC3PY1OH3fjY7' +
                      'Wtov4JFi7Ze1luBMWJuB1ZpLKHDDVmbV9OzzsQvmv5' +
                      'ABpb88V3OGMthaVNT6U5TpSiB8g0ZJ0FzdhAXZ_sqn' +
                      'onrg5ZY7tZQd1I2dMUjQ')
}

auth_header_client = {
    'Authorization': ('Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtp' +
                      'ZCI6IkdaOGJ6anR4RVpyQ2gwY0V2OHJuVCJ9.eyJpc3MiOi' +
                      'JodHRwczovL25pY2guZXUuYXV0aDAuY29tLyIsInN1YiI6Im' +
                      'F1dGgwfDVlYTdhZDY1NmM4ZWIyMGMxNTM0OWUxZCIsImF1ZCI' +
                      '6ImNhcHN0b25lIiwiaWF0IjoxNTg4MTM1NDE1LCJleHAiOjE1' +
                      'ODgyMjE4MTUsImF6cCI6IkdSaHRWSk9KZm5aQjZZMmRMUnhWdE' +
                      'RzR05IOElMS3pIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6' +
                      'WyJkZWxldGU6Y2xpZW50cyIsImdldDpwcm9kdWN0cyIsInBhdG' +
                      'NoOmNsaWVudHMiLCJwb3N0OmNsaWVudHMiXX0.JpUxcaIA79xI' +
                      'AuINKeHrnfn_Y2qdVIrOnITmZ3mREEl0Y0fXXiju3EvcuHhXlh' +
                      'UJQjW-55G_TNHZ1vj6MIWJxuiFd_zwJHkoMo50rOH0nbhgLDLn' +
                      'VZ48L5_BTV0P6ARqZ78r-aNap-ryD72b4A7mPugeitZcVGCOF6' +
                      'hDuOxrLk8JZQBE7QDS4GU7TdDSrcpAT6dUCqaS8XtyPSKEsWZU9' +
                      'ruuJUbEDtc_oMnjvfr8UXppX9wzL_lFcB58tTrJk1TcWc2Nd39v' +
                      '0M-7QTwAqDc82LPN9batYcHXLY0bNjmzxMULTs4UJkvwObp3zMr' +
                      'G-Fx0gZr6hsKc5XN6Voxddo0aBQ')
}

new_client_id = 1
new_product_id = 10


class CapstoneTestCase(unittest.TestCase):
    """
    This class represents the test cases
    of resources of the FSND Capstone project
    """

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = ("postgres://upjcrmjyvdqdmu:729ab9adc43d492" +
                              "4df23fb0f4795787ab6d73bf709b63114deadb004" +
                              "cc026ea4@ec2-18-235-20-228.compute-1.amaz" +
                              "onaws.com:5432/ddr6r33e7bl6qp")
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
