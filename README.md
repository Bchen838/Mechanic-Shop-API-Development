# Mechanic Shop API

A Flask REST API for managing a small mechanic shop. This project allows users to manage customers, mechanics, service tickets, and inventory items. It also includes customer token authentication, advanced relationship endpoints, caching, rate limiting, pagination, interactive API documentation, and automated route testing. 

## Project Overview

This API was built to practice backend development concepts including:
- Flask routing
- Application Factory Pattern
- Blueprints
- SQLAlchemy ORM models and relationships
- Marshmallow serialization and validation
- MySQL database integration
- Many-to-many relationships
- Token authentication with JWTs
- Caching and rate limiting
- Pagination
- Interactive Swagger documentation
- Automated unit testing with unittest

---

## The main resources in this project are:

- Customers
- Mechanics
- Service Tickets
- Inventory 

---

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
- Python-Jose
- Flask-Caching
- Flask-Limiter
- Unittest
- Swagger

## Features

### Customers

- Create a customer
- Retrieve all customers
- Retrieve a specific customer by ID
- Update customer information
- Delete a customer
- Paginate customer results
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

### Inventory

- Create an inventory item
- Retrieve all inventory items
- Retrieve a specific inventory item by ID
- Update inventory item information
- Delete an inventory item

### Authentication

This project includes token authentication for protected customer routes. Customers can log in using their email and password. If credentials are valid, the API will return an authentication token which must be included in the Authorization as a Bearer token when trying to access protected routes. 

The protected routes include:
- GET /customers/my-tickets
- PUT /customers/
- DELETE /customers/
