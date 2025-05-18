import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_name_initialization():
    with pytest.raises(TypeError):
        coffee = Coffee(123)
    with pytest.raises(ValueError):
        coffee = Coffee("AB")

def test_coffee_orders_and_customers():
    Order.all_orders = []

    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")

    order1 = Order(customer1, coffee1, 4.0)
    order2 = Order(customer2, coffee1, 5.0)
    order3 = Order(customer1, coffee2, 3.0)

    coffee1_orders = coffee1.orders()
    coffee2_orders = coffee2.orders()

    assert len(coffee1.orders()) == 2
    assert order1 in coffee1_orders
    assert order2 in coffee1_orders
    assert order3 not in coffee1_orders

    assert coffee2_orders == [order3]
    
    coffee1_customers = coffee1.customers()
    coffee2_customers = coffee2.customers()

    assert len(coffee1_customers) == 2
    assert customer1 in coffee1_customers
    assert customer2 in coffee1_customers
    assert customer1 in coffee2_customers
    assert customer2 not in coffee2_customers

    assert coffee2_customers == [customer1]

def test_num_orders_and_avg_price():
    Order.all_orders = []

    coffee   = Coffee("Espresso")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")

    customer1.create_order(coffee, 4.0)
    customer2.create_order(coffee, 6.0)
    customer1.create_order(coffee, 5.0)

    assert coffee.num_orders() == 3
    assert coffee.average_price() == 5.0
