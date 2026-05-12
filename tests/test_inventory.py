from app import create_app
from app.models import db, Mechanic, Service_Ticket, Customer, Inventory
import unittest
from datetime import date


class TestMechanic(unittest.TestCase):
    def setUp(self):
        self.app = create_app("TestingConfig")

        self.inventory = Inventory(
            name="Brake Pads",
            price=89.99
        )


        with self.app.app_context():
            db.drop_all()
            db.create_all()
            db.session.add(self.inventory)
            db.session.commit()
        self.client = self.app.test_client()


    def test_create_inventory(self):
        inventory_payload = {
            "name": "Oil Filter",
            "price": 14.99
        }

        response = self.client.post('/inventory/', json=inventory_payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], "Oil Filter")

    
    def test_get_all_inventory(self):
        response = self.client.get('/inventory/')

        self.assertEqual(response.status_code, 200)


    def test_get_inventory_by_id(self):
        response = self.client.get('/inventory/1')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 1)
        self.assertEqual(response.json['name'], "Brake Pads")


    def test_update_inventory(self):
        update_payload = {
            "price": 99.99
        }

        response = self.client.put('/inventory/1', json=update_payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['price'], 99.99)


    def test_delete_inventory(self):
        response = self.client.delete('/inventory/1')

        self.assertEqual(response.status_code, 200)