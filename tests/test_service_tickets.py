from app import create_app
from app.models import db, Mechanic, Service_Ticket, Customer, Inventory
import unittest
from datetime import date


class TestMechanic(unittest.TestCase):
    def setUp(self):
        self.app = create_app("TestingConfig")
        self.customer = Customer(
            name="Brian",
            email="brian@email.com",
            number="415-999-9999",
            password="123456"
        )

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

        self.inventory = Inventory(
            name="Brake Pads",
            price=89.99
        )

        self.service_ticket = Service_Ticket(
            customer_id=1,
            vin="GDF7896FG7896H",
            service_desc="Oil change and brake inspection",
            service_date=date(2026,5,11)
        )


        with self.app.app_context():
            db.drop_all()
            db.create_all()
            db.session.add(self.mechanic)
            db.session.add(self.mechanic2)
            db.session.add(self.customer)
            db.session.add(self.inventory)
            db.session.add(self.service_ticket)
            db.session.commit()
        self.client = self.app.test_client()


    def test_create_service_ticket(self):
        service_ticket_payload = {
            "customer_id": 1,
            "vin": "8df76gdf78g",
            "service_desc": "Tire rotation",
            "service_date": "2026-05-12"
        }

        response = self.client.post('/service-tickets/', json=service_ticket_payload)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['customer_id'], 1)
        self.assertEqual(response.json['service_desc'], "Tire rotation")

    
    def test_get_all_service_tickets(self):
        response = self.client.get('/service-tickets/')

        self.assertEqual(response.status_code, 200)


    def test_assign_mechanic_to_service_ticket(self):
        response = self.client.put('/service-tickets/1/assign-mechanic/1')

        self.assertEqual(response.status_code, 200)


    def test_remove_mechanic_from_service_ticket(self):
        self.client.put('/service-tickets/1/assign-mechanic/1')

        response = self.client.put('/service-tickets/1/remove-mechanic/1')

        self.assertEqual(response.status_code, 200)


    def test_edit_service_ticket_mechanics(self):
        edit_payload = {
            "add_mechanic_ids": [1,2],
            "remove_mechanic_ids": []
        }

        response = self.client.put('/service-tickets/1/edit', json=edit_payload)

        self.assertEqual(response.status_code, 200)

    
    def test_add_inventory_part_to_service_ticket(self):
        response = self.client.put('/service-tickets/1/add-part/1')

        self.assertEqual(response.status_code, 200)

    def test_create_service_ticket_invalid_customer(self):
        service_ticket_payload = {
            "customer_id": 999,
            "vin": "8df76gdf78g",
            "service_desc": "Tire rotation",
            "service_date": "2026-05-12"
        }

        response = self.client.post('/service-tickets/', json=service_ticket_payload)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], "Customer not found.")


    def test_assign_mechanic_to_invalid_ticket(self):
        response = self.client.put('/service-tickets/999/assign-mechanic/1')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], "Service Ticket not found.")


    def test_assign_duplicate_mechanic_to_service_ticket(self):
        self.client.put('/service-tickets/1/assign-mechanic/1')

        response = self.client.put('/service-tickets/1/assign-mechanic/1')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json['error'],
            "Mechanic is already assigned to this ticket."
        )


    def test_add_inventory_to_invalid_service_ticket(self):
        response = self.client.put('/service-tickets/999/add-part/1')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], "Service Ticket not found.")