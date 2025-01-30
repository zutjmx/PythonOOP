# Se importa Faker
from faker import Faker
fake = Faker('es_MX')

# Se crean unas variables con datos falsos
nombre = fake.name()
edad = fake.random_int(min=18, max=99)
email = fake.email()
direccion = fake.address()

# Se imprimen los datos
print(f"Se imprimen los datos falsos")
print(f"Nombre: {nombre.upper()}")
print(f"Edad: {edad}")
print(f"Email: {email}")
print(f"Dirección: {direccion}")

print(f"Se imprimen los tipos de datos")
print(type(nombre))
print(type(edad))
print(type(email))
print(type(direccion))

# Se define una clase llamada Perro
class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        
    def ladra(self):
        print("Guau, guau")

# Se crea un objeto de la clase Perro
trotsky = Perro(fake.name(),fake.company(),fake.random_int(min=1, max=10))
trotsky.ladra()

estela = Perro(fake.name(),fake.company(), fake.random_int(min=1, max=10))
estela.ladra()
