import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app
from models import setup_db, Client, Product, database_path


class CapstoneTestCase(unittest.TestCase):
    """This class represents the test case of resources on the Capstone project"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "test_db"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_client = {
            "first_name": "Yvonne",
            "surname": "Jansen van Rensburg",
            "id_number": "1804170199087",
            "email": "yvonne.vanrensburg@gmail.com",
            "phone": "0124603178"
        }

        self.new_product = {
            "name": "Project finance",
            "description": "A project financed loan to the client",
            "price": 12.40
        }
    

    def tearDown(self):
        """Executed after reach test"""
        pass

    
    def test_get_products(self):
        """Test for the "GET /products endpoint handler"""
        res = self.client().get('/products')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['products']))
        self.assertTrue(data['total products'])

    '''
    def test_404_get_products(self):
        """Test for the "GET /questions endpoint handler"""
        res = self.client().get('/products?')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['categories']))


    def test_play_quiz_game(self):
        """Tests playing quiz game success"""
        self.new_quiz = {'previous_questions': [1, 2],
                        'quiz_category': {'type': 'Science', 'id': '1'}}
        
        res = self.client().post('/quizzes', json= self.new_quiz)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
        self.assertEqual(data['question']['category'], 1)
        self.assertNotEqual(data['question']['id'], 1)
        self.assertNotEqual(data['question']['id'], 2)

    # This test is now deactivated as the specific id has been deleted
    #def test_delete_questions(self):
    
    #   """Test for the DELETE /questions endpoint handler where a 
    #    specific question is to be deleted"""

    #    q_id = 9
    #    res = self.client().delete('/questions/{}'.format(q_id))
    #    data = json.loads(res.data)

    #    question = Question.query.filter(Question.id == q_id).one_or_none()

    #    self.assertEqual(res.status_code, 200)
    #    self.assertEqual(data['success'], True)
    #    self.assertEqual(data['deleted'],q_id)
    #    self.assertTrue(len(data['questions']))
    #    self.assertTrue(data['total_questions'])
    #    self.assertEqual(question, None)


    def test_create_new_question(self):
        """Test for the creation of a new book"""
        self.new_question = {
            'question': 'Where in the world is Wally?',
            'answer': 'In a book',
            'category': 4,
            'difficulty': 5
        }

        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['questions']))

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