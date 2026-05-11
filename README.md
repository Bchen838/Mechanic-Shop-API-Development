# Mechanic Shop API

A Flask REST API for managing a small mechanic shop. This project allows users to manage customers, mechanics, service tickets, and inventory items. It also supports assigning and removing mechanics from service tickets using many-to-many relationships.

## Project Overview

This API was built to practice database design, Flask routing, Marshmallow serialization/deserialization, SQLAlchemy ORM relationships, MySQL integration, Blueprints, and the Application Factory Pattern.

The main resources in this project are:

- Customers
- Mechanics
- Service Tickets
- Inventory Parts

A customer can have many service tickets. A service ticket belongs to one customer. A service ticket can have many mechanics assigned to it, and a mechanic can work on many service tickets. A service ticket can also require many inventory parts and the same inventory part can be used on many service tickets. 

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
- Python Jose
- Flask-Caching
- Flask-Limiter

## Features

### Customers

- Create a customer
- Retrieve all customers
- Retrieve a specific customer by ID
- Update customer information
- Delete a customer
- Paginate get all customer
- Customer login with token authentication
- Retrieve a customer's service tickets using a protected route

### Mechanics

- Create a mechanic
- Retrieve all mechanics or by ID
- Update mechanic information
- Delete a mechanic
- Retrieve mechanics ordered by who has worked on the most service tickets

### Service Tickets

- Create a service ticket
- Retrieve all service tickets or by ID
- Assign a mechanic to a service ticket
- Remove a mechanic from a service ticket
- Add and remove multiple mechanics from a service ticket in one request
- Add an inventory part to a service ticket

### Authentication

This project includes token authentication for protected customer routes. Customers can log in using their email and passowrd. If credentials are valid, the API will return an authentication token which must be included in the Authorization as a Bearer token when trying to access protected routes. 

The protected routes include:
- GET /customers/service-tickets
- PUT /customers
- DELETE /customers
