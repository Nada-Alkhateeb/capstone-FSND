import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
import os

from app import create_app
from models import setup_db, movies, actors

producer_auth = {
    'Content-Type': 'application/json',
    'Authorization': os.getenv('PRODUCER_AUTH')
}

assistant_auth = {
    'Content-Type': 'application/json',
    'Authorization': os.getenv('ASSISTANT_AUTH')
}

director_auth = {
    'Content-Type': 'application/json',
    'Authorization': os.getenv('DIRECTOR_AUTH')
}


class TestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.getenv('DATABASE_URL')

        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    test for each test for successful operation and for expected errors.
    """

    def test_retrive_actors(self):
        res = self.client().get('/actors', headers=assistant_auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['total']))

    def test_retrieve_actors_failure(self):
        res = self.client().post('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    def test_retrive_movies(self):
        res = self.client().get('/movies', headers=assistant_auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['total']))

    def test_retrive_movies_failure(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    def test_delete_actors(self):
        res = self.client().delete('/actors/2', headers=producer_auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 2)

    def test_delete_actors_failure(self):
        res = self.client().delete('/actors/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    def test_delete_movies(self):
        res = self.client().delete('/movies/2', headers=producer_auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 2)

    def test_delete_movies_failure(self):
        res = self.client().delete('/movies/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    def test_add_actors(self):
        actor = {
            "name": 'Roz',
            "age": '22',
            "gender": 'F'
        }
        res = self.client().post('/actors', headers=producer_auth, json=actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_add_actors_failure(self):
        actor = {
            "name": 'Roz',
            "age": '22'
        }

        res = self.client().post('/actors', headers=producer_auth, json=actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_add_movies(self):
        movie = {
            "title": 'Up',
            "release_date": '11-3-1017'
        }
        res = self.client().post('/movies', headers=producer_auth, json=movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_add_movies_failure(self):
        movie = {
            "title": 'Up'
        }
        res = self.client().post('/movies', headers=producer_auth, json=movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_patch_actors(self):
        actor = {"name": "Jo"}
        res = self.client().patch('/actors/1', headers=producer_auth,
                                  json=actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_patch_actors_failure(self):
        actor = {"name": "Jo"}
        res = self.client().patch('/actors/1', json=actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    def test_patch_movies(self):
        movie = {"title": "Up"}
        res = self.client().patch('/movies/1', headers=producer_auth, json=movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_patch_movies_failure(self):
        movie = {"title": "Up"}
        res = self.client().patch('/movies/1', json=movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
