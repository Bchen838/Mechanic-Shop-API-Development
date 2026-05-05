# Mechanic Shop API

A Flask REST API for managing a small mechanic shop. This project allows users to manage customers, mechanics, and service tickets. It also supports assigning and removing mechanics from service tickets using many-to-many relationships.

## Project Overview

This API was built to practice database design, Flask routing, Marshmallow serialization/deserialization, SQLAlchemy ORM relationships, MySQL integration, Blueprints, and the Application Factory Pattern.

The main resources in this project are:

- Customers
- Mechanics
- Service Tickets

A customer can have many service tickets. A service ticket belongs to one customer. A service ticket can have many mechanics assigned to it, and a mechanic can work on many service tickets.

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy ORM
- Flask-Marshmallow
- Marshmallow
- MySQL
- MySQL Connector
- Postman

## Features

### Customers

- Create a customer
- Retrieve all customers
- Retrieve a specific customer by ID
- Update customer information
- Delete a customer

### Mechanics

- Create a mechanic
- Retrieve all mechanics
- Update mechanic information
- Delete a mechanic

### Service Tickets

- Create a service ticket
- Retrieve all service tickets
- Assign a mechanic to a service ticket
- Remove a mechanic from a service ticket
