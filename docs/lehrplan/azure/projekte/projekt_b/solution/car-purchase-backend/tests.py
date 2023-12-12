import unittest
from flask_testing import TestCase
import app
from config import db, app
from models import CarModel, CarType


# Create a test class that inherits from Flask-Testing's TestCase
class APITestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_car_models(self):
        # Create some test data
        car1 = CarModel(name='Toyota', price=300, image="")
        car2 = CarModel(name='Honda', price=500, image="")
        db.session.add_all([car1, car2])
        db.session.commit()

        # Make a request to the API endpoint that fetches the list of car models
        response = self.client.get('/car-models')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected data
        data = response.json
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], 'Toyota')
        self.assertEqual(data[0]['price'], 300)
        self.assertEqual(data[1]['name'], 'Honda')
        self.assertEqual(data[1]['price'], 500)

    def test_get_car_types(self):
        # Create some test data
        type1 = CarType(name='Petrol', price=300)
        type2 = CarType(name='Diesel', price=500)
        db.session.add_all([type1, type2])
        db.session.commit()

        # Make a request to the API endpoint that fetches the list of types
        response = self.client.get('/car-types')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected data
        data = response.json
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], 'Petrol')
        self.assertEqual(data[0]['price'], 300)
        self.assertEqual(data[1]['name'], 'Diesel')
        self.assertEqual(data[1]['price'], 500)


if __name__ == '__main__':
    unittest.main()
