# Se importa Faker
from faker import Faker
fake = Faker('es_MX')

# How to create a class:
class Item:
    def calculate_total_price(self, x, y):
        return x * y

# How to create an instance of a class
item1 = Item()

# Assign attributes:
item1.name = fake.company().upper()
print('Item uno: ',item1.name)
item1.price = 100
print('Precio Item uno: ',item1.price)
item1.quantity = 5
print('Cantidad Item uno: ',item1.quantity)

# Calling methods from instances of a class:
print('Total Item uno: ',item1.calculate_total_price(item1.price, item1.quantity))

# How to create an instance of a class (We could create as much as instances we'd like to)
item2 = Item()

# Assign attributes
item2.name = fake.company().upper()
print('Imtem dos: ',item2.name)
item2.price = 1000
print('Precio Item uno: ',item2.price)
item2.quantity = 3
print('Cantidad Item uno: ',item2.quantity)

# Calling methods from instances of a class: 
print('Total Item dos: ',item2.calculate_total_price(item2.price, item2.quantity))
