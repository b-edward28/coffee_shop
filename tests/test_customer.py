import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_initialization():
    with pytest.raises(TypeError):
        customer = Customer(123)
    with pytest.raises(ValueError):
        customer = Customer("A" * 16)

def test_customer_orders_and_coffee():
    Order.all_orders = []

    customer = Customer("Alice")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")

    order1 = Order(customer, coffee1, 5.0)
    order2 = Order(customer, coffee2, 4.0)

    customer_orders = customer.orders()
    assert order1 in customer_orders
    assert order2 in customer_orders
    assert len(customer_orders) == 2

    coffees = customer.coffee()
    assert coffee1 in coffees
    assert coffee2 in coffees
    assert len(coffees) == 2

def test_customer_most_aficionado():
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")

    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")

    order1 = Order(customer1, coffee1, 5.0)
    order2 = Order(customer1, coffee2, 4.5)
    order3 = Order(customer2, coffee1, 6.0)

    assert Customer.most_aficionado(coffee1) == customer2
    assert Customer.most_aficionado(coffee2) == customer1
    assert Customer.most_aficionado(Coffee("Nonexistent")) is None