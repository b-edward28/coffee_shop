# Coffee Shop Domain Model
## Overview
This is a Python-based object-oriented programming project that models a coffee shop's domain, capturing the relationships and interactions between customers, coffees, and orders.

The goal is to demonstrate understanding of OOP concepts such as encapsulation, association,dependency, data validation, and unit testing using Python.

## Installation
### 1. Clone this repository
git clone this repo
cd coffee_shop

### 2. To set up virtual environment run the codes below
pipenv install
pipenv shell

### 3. Install pytest
pipenv install pytest

## Domain Model
### Classes

#### Customer
It has attribute name 
Methods include; orders(), coffee(), create_order(), most_aficionado(coffee)

#### Coffee
It has the attribute name
Methods include: orders(), customers(), num_orders(), average_price()

#### Order
It has the attribute customer, coffee, price

### Relationships
- A customer can have many orders
- A coffee can have many orders
- An order belongs to one customer and one coffee
- Customer and coffee have many to many relationships

### Features
1. Encapsulation - using setter methods
2. Association - A Customer is associated with multiple orders.
                 A Coffee is associated with multiple orders.
3. Dependency - In Customer.create_order(coffee, price)
4. Unit testing using pytest
5. Data validation

### Running test
Making sure you are in the virtual environment run "pytest"




