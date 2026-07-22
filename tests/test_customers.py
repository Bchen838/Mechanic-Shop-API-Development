from app import create_app
from app.models import db, Customer
from app.utils.util import encode_token
from datetime import date
from werkzeug.security import generate_password_hash
import unittest

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.app = create_app("TestingConfig")
        self.customer = Customer(
            name="Brian",
            email="brian@email.com",
            number="415-999-9999",
            password=generate_password_hash("123456")
        )

        with self.app.app_context():
            db.drop_all()
            db.create_all()
            db.session.add(self.customer)
            db.session.commit()
        self.token = encode_token(1)
        self.client = self.app.test_client()


    def test_create_customer(self):
        customer_payload = {
            "name": "New Customer",
            "email": "newcustomer@email.com",
            "number": "415-333-3333",
            "password": "password123"
        }

        response = self.client.post('/customers/', json=customer_payload)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], "New Customer")


    def test_invalid_customer_creation(self):
        customer_payload = {
            "name": "Invalid Customer",
            "number": "415-333-3333",
            "password": "password123"
        }

        response = self.client.post('/customers/', json=customer_payload)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['email'], ['Missing data for required field.'])


    def test_get_all_customers(self):
        response = self.client.get('/customers/')

        self.assertEqual(response.status_code, 200)


    def test_get_customer_by_id(self):
        response = self.client.get('/customers/1')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 1)
        self.assertEqual(response.json['name'], "Brian")


    def test_login_customer(self):
        credentials = {
            "email": "brian@email.com",
            "password": "123456"
        }

        response = self.client.post('/customers/login', json=credentials)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], "success")
        return response.json['auth_token']


    def test_get_my_tickets(self):

        headers = {'Authorization': "Bearer " + self.test_login_customer()}
        response = self.client.get('/customers/my-tickets', headers=headers)

        self.assertEqual(response.status_code, 200)


    def test_get_my_tickets_without_token(self):
        response = self.client.get('/customers/my-tickets')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['message'], "Token is missing!")


    def test_update_customer(self):
        update_payload = {
            "name": "Updated Brian"
        }

        headers = {'Authorization': "Bearer " + self.test_login_customer()}

        response = self.client.put(
            '/customers/',
            json=update_payload,
            headers=headers
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], "Updated Brian")


    def test_delete_customer(self):

        headers = {'Authorization': "Bearer " + self.test_login_customer()}
        response = self.client.delete('/customers/', headers=headers)

        self.assertEqual(response.status_code, 200)

    