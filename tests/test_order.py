import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_initialization():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 5.0)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_price_validation():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")

    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  # Price too low
    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0)  # Price too high