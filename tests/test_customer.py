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
    customer = Customer("Alice")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")
    order1 = Order(customer, coffee1, 5.0)
    order2 = Order(customer, coffee2, 4.5)

    assert customer.orders() == [order1, order2]
    assert customer.coffee() == [coffee1, coffee2]
    assert customer.create_order(coffee1, 5.0) == order1
    assert customer.create_order(coffee2, 4.5) == order2
    assert customer.create_order(coffee1, 5.0).price == 5.0
    assert customer.create_order(coffee2, 4.5).price == 4.5

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