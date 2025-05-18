# Coffee Shop Domain Model
## Overview
This is a Python-based object-oriented programming project that models a coffee shop's domain, capturing the relationships and interactions between customers, coffees, and orders.

The goal is to demonstrate understanding of OOP concepts such as encapsulation, association,dependency, data validation, and unit testing using Python.

## Installation
### 1. Clone this repository
- git clone this repo
- cd coffee_shop

### 2. To set up virtual environment run the codes below
     * pipenv install
     * pipenv shell

### 3. Install pytest
pipenv install pytest

## File Structure
coffee_shop/
 - customer.py
 - coffee.py
 - order.py
 - debug.py
 - tests/
     - test_customer.py
     - test_coffee.py
     - test_order.py
 - README.md

## Domain Model
### Create Classes
Create three Python files in your project directory and in each file, define a class corresponding to the file name:
 - customer.py
 - coffee.py
 - order.py

#### Customer
- It has attribute - name with a string between 1 and 15 characters.
- Methods include; orders(), coffee(), create_order(), most_aficionado(coffee)

#### Coffee
- It has the attribute - name with a string, at least 3 characters long.
- Methods include: orders(), customers(), num_orders(), average_price()

#### Order
It has Customer instance, a Coffee instance, and a price (float between 1.0 and 10.0)

### Relationships
- A customer can have many orders
- A coffee can have many orders
- An order belongs to one customer and one coffee
- Customer and coffee have many to many relationships

### Features
1. Encapsulation - using setter methods
2. Association - A Customer is associated with multiple orders and a Coffee is associated with multiple orders.
3. Dependency - In Customer.create_order(coffee, price)
4. Unit testing using pytest
5. Data validation

### Running test
* Create a tests directory in your project directory.
* Add test files (test_customer.py, test_coffee.py, test_order.py) to test each class and method.
* Write test cases to validate that each method and property works correctly.
* Making sure you are in the virtual environment run "pytest"

### Debugging
Create a debug.py file to test your code interactively.
