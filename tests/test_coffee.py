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
    coffee = Coffee("Espresso")
    customer = Customer("Alice")

    assert len(coffee.orders()) == 1
    assert customer in coffee.customers()

def test_num_orders_and_avg_price():
    coffee = Coffee("Espresso")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")

    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 4.5)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 4.75
