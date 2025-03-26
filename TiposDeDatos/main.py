# Se importa Faker
from faker import Faker
fake = Faker('es_MX')

# Declarar el tipo de dato está de más
edad:int = fake.random_int(min=18, max=65)
print(edad)

# Declarar el tipo de dato está de más
nombre:str = fake.name()
print(nombre)
