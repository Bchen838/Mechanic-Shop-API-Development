from .schemas import service_ticket_schema, service_tickets_schema, edit_service_ticket_schema
from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from app.models import Service_Ticket, db, Customer, Mechanic, Inventory
from . import service_tickets_bp 


# CREATE Service Ticket
@service_tickets_bp.route('/', methods=['POST'])
def create_service_ticket():
    try:
        ticket_data = service_ticket_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer = db.session.get(Customer, ticket_data['customer_id'])
    if not customer:
        return jsonify({"error": "Customer not found."}), 404
    
    new_ticket = Service_Ticket(**ticket_data)
    db.session.add(new_ticket)
    db.session.commit()
    return service_ticket_schema.jsonify(new_ticket), 201

# GET all Service Tickets
@service_tickets_bp.route('/', methods=['GET'])
def get_service_tickets():
    query = select(Service_Ticket)
    tickets = db.session.execute(query).scalars().all()
    return service_tickets_schema.jsonify(tickets), 200

# UPDATE Service Ticket to assign mechanic
@service_tickets_bp.route('/<int:ticket_id>/assign-mechanic/<int:mechanic_id>', methods=['PUT'])
def assign_mechanic(ticket_id, mechanic_id):
    ticket = db.session.get(Service_Ticket, ticket_id)

    if not ticket:
        return jsonify({"error": "Service Ticket not found."}), 404
    
    mechanic = db.session.get(Mechanic, mechanic_id)

    if not mechanic:
        return jsonify({"error": "Mechanic not found."}), 404
    
    if mechanic in ticket.mechanics:
        return jsonify({"error": "Mechanic is already assigned to this ticket."}), 400
    
    ticket.mechanics.append(mechanic)
    db.session.commit()

    return service_ticket_schema.jsonify(ticket), 200

# UPDATE Service Ticket to unassign mechanic
@service_tickets_bp.route('/<int:ticket_id>/remove-mechanic/<int:mechanic_id>', methods=['PUT'])
def remove_mechanic(ticket_id, mechanic_id):
    ticket = db.session.get(Service_Ticket, ticket_id)

    if not ticket:
        return jsonify({"error": "Service ticket not found."}), 404
    
    mechanic = db.session.get(Mechanic, mechanic_id)

    if not mechanic:
        return jsonify({"error": "Mechanic not found."}), 404
    
    if mechanic not in ticket.mechanics:
        return jsonify({"error": "Mechanic is not assigned to this ticket."}), 400

    ticket.mechanics.remove(mechanic)
    db.session.commit()
    return service_ticket_schema.jsonify(ticket), 200


# Route to add AND remove mechanics from a ticket 
@service_tickets_bp.route('/<int:ticket_id>/edit', methods=['PUT'])
def edit_ticket_mechanics(ticket_id):
    try:
        ticket_edits = edit_service_ticket_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    
    query = select(Service_Ticket).where(Service_Ticket.id == ticket_id)
    ticket = db.session.execute(query).scalars().first()

    for mechanic_id in ticket_edits['add_mechanic_ids']:
        query = select(Mechanic).where(Mechanic.id == mechanic_id)
        mechanic = db.session.execute(query).scalars().first()

        if mechanic and mechanic not in ticket.mechanics:
            ticket.mechanics.append(mechanic)

    
    for mechanic_id in ticket_edits['remove_mechanic_ids']:
        query = select(Mechanic).where(Mechanic.id == mechanic_id)
        mechanic = db.session.execute(query).scalars().first()

        if mechanic and mechanic in ticket.mechanics:
            ticket.mechanics.remove(mechanic)
    db.session.commit()
    return service_ticket_schema.jsonify(ticket), 200


# ADD Inventory Part to Service Ticket
@service_tickets_bp.route('/<int:ticket_id>/add-part/<int:inventory_id>', methods=['PUT'])
def add_part_to_tickets(ticket_id, inventory_id):
    ticket = db.session.get(Service_Ticket, ticket_id)
    if not ticket:
        return jsonify({'error': 'Service ticket not found.'}), 404
    
    part = db.session.get(Inventory, inventory_id)

    if not part:
        return jsonify({'error': 'Inventory part not found'}), 404

    if part in ticket.inventory:
        return jsonify({'error': 'Part is already assigned to this ticket.'}), 400
    
    ticket.inventory.append(part)
    db.session.commit()

    return service_ticket_schema.jsonify(ticket), 200