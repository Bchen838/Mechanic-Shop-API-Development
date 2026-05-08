from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from app.models import Inventory, db
from . import inventory_bp
from .schemas import inventory_schema, inventories_schema


# CREATE Inventory Part
@inventory_bp.route('/', methods=['POST'])
def create_inventory():
    try:
        inventory_data = inventory_schema.load(request.get_json())
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_part = Inventory(**inventory_data)

    db.session.add(new_part)
    db.session.commit()

    return inventory_schema.jsonify(new_part), 201


# GET all Inventory Parts
@inventory_bp.route('/', methods=['GET'])
def get_inventory():
    query = select(Inventory)
    inventory = db.session.execute(query).scalars().all()

    return inventories_schema.jsonify(inventory), 200


# GET Specific Inventory Part
@inventory_bp.route('/<int:inventory_id>', methods=['GET'])
def get_inventory_item(inventory_id):
    inventory_item = db.session.get(Inventory, inventory_id)

    if not inventory_item:
        return jsonify({"error": "Inventory item not found."}), 404

    return inventory_schema.jsonify(inventory_item), 200


# UPDATE Inventory Part
@inventory_bp.route('/<int:inventory_id>', methods=['PUT'])
def update_inventory(inventory_id):
    inventory_item = db.session.get(Inventory, inventory_id)

    if not inventory_item:
        return jsonify({"error": "Inventory item not found."}), 404

    try:
        inventory_data = inventory_schema.load(request.get_json(), partial=True)
    except ValidationError as e:
        return jsonify(e.messages), 400

    for key, value in inventory_data.items():
        setattr(inventory_item, key, value)

    db.session.commit()

    return inventory_schema.jsonify(inventory_item), 200


# DELETE Inventory Part
@inventory_bp.route('/<int:inventory_id>', methods=['DELETE'])
def delete_inventory(inventory_id):
    inventory_item = db.session.get(Inventory, inventory_id)

    if not inventory_item:
        return jsonify({"error": "Inventory item not found."}), 404

    db.session.delete(inventory_item)
    db.session.commit()

    return jsonify({"message": f"Inventory item id: {inventory_id}, successfully deleted."}), 200