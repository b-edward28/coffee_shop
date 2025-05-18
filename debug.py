from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
bob = Customer("Bob")

espresso = Coffee("Espresso")
latte = Coffee("Latte")
cappuccino = Coffee("Cappuccino")

order1 = alice.create_order(latte), 4.0)
order2 = bob.create_order(latte, 5.0)
order3 = alice.create_order(espresso, 6.0)

print(latte.customers())
print(alice.coffee())
print(Coffee("Latte").average_price())
print(Coffee("Mocha").average_price())