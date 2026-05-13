# Mechanic Shop API

A Flask REST API for managing a small mechanic shop. This project allows users to manage customers, mechanics, service tickets, and inventory items. It also includes customer token authentication, advanced relationship endpoints, caching, rate limiting, pagination, interactive API documentation, and automated route testing. 

## Project Overview

This API was built to practice backend development concepts including:
- Flask routing
- Application Factory Pattern
- Blueprints
- SQLAlchemy ORM models and relationships
- Marshmallow serialization and validation
- MySQL development database and PostgreSQL production database integration
- Many-to-many relationships
- Token authentication with JWTs
- Caching and rate limiting
- Pagination
- Interactive Swagger documentation
- Automated unit testing with unittest
- Production deployment with Render
- CI/CD automation using GitHub Actions

---

## Main Resources

The main resources in this project are:

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
- `unittest`
- Swagger
- Gunicorn
- GitHub Actions
- PostgreSQL
- psycopg2

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
- Retrieve all mechanics
- Retrieve a specific mechanic by ID
- Update mechanic information
- Delete a mechanic
- Retrieve mechanics ordered by who has worked on the most service tickets

### Service Tickets

- Create a service ticket
- Retrieve all service tickets
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

This project includes token authentication for protected customer routes. Customers can log in using their email and password. If credentials are valid, the API returns an authentication token, which must be included in the `Authorization` header as a Bearer token when trying to access protected routes. 

The protected routes include:
- `GET /customers/my-tickets`
- `PUT /customers/`
- `DELETE /customers/`

### Testing

Automated route tests were written using Python's built-in unittest framework. 
The test suite covers:
- Customer, Mechanic, Service Ticket, and Inventory CRUD operations
- Customer login
- Negative tests for missing or invalid data
- Service ticket creation and mechanic assignment

Tests can be run with:
```console
python -m unittest discover tests
```

### API Documentation

This project includes interactive Swagger documentation for exploring and testing the API endpoints directly in the browser. Swagger documentation was updated for deployment so that it uses the live API host and HTTPS scheme.
The documentation includes:
- Available routes
- Required request payloads
- Response models
- Authentication requirements
- Interactive endpoint testing

### Deployment

This API was configured for production deployment on Render. The production configuration:
- Uses a hosted PostgreSQL database
- Retrieves private values through environment variables
- Supports deployment through Gunicorn

### CI/CD Pipeline

The pipeline is designed to:
1. Trigger when changes are pushed to the repository
2. Install dependencies
3. Run the automated unit test suite
4. Deploy the application to Render only if all tests pass
