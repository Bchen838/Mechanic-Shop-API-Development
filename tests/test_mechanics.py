from app import create_app
from app.models import db, Mechanic
import unittest

class TestMechanic(unittest.TestCase):
    def setUp(self):
        self.app = create_app("TestingConfig")
        self.mechanic = Mechanic(
            name="Alex",
            email="alex@email.com",
            phone="444-555-6666",
            salary=65000.00
        )

        self.mechanic2 = Mechanic(
            name="Sam",
            email="sam@email.com",
            phone="222-333-4444",
            salary=70000.00
        )

        with self.app.app_context():
            db.drop_all()
            db.create_all()
            db.session.add(self.mechanic)
            db.session.add(self.mechanic2)
            db.session.commit()
        self.client = self.app.test_client()



    def test_create_mechanic(self):
        mechanic_payload = {
            "name": "Chris",
            "email": "chris@email.com",
            "phone": "415-444-4444",
            "salary": 72000.00
        }

        response = self.client.post('/mechanics/', json=mechanic_payload)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], "Chris")

    def test_invalid_create_mechanic(self):
        mechanic_payload = {
            "name": "Chris",
            "email": "chris@email.com",
            "phone": "415-444-4444"
        }

        response = self.client.post('/mechanics/', json=mechanic_payload)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['salary'], ['Missing data for required field.'])

    
    def test_get_all_mechanics(self):
        response = self.client.get('/mechanics/')

        self.assertEqual(response.status_code, 200)


    def test_update_mechanic(self):
        update_payload = {
            "name": "Updated Alex"
        }

        response = self.client.put('/mechanics/1', json=update_payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], "Updated Alex")


    def test_delete_mechanic(self):
        response = self.client.delete('/mechanics/1')

        self.assertEqual(response.status_code, 200)


    def test_most_active_mechanics(self):
        self.client.put('/service-tickets/1/assign-mechanic/1')
        response = self.client.get('/mechanics/most-active')

        self.assertEqual(response.status_code, 200)


    