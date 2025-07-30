# Se importa Faker
from faker import Faker
fake = Faker('es_MX')

print("Tipos de Datos, Generación de Datos Falsos")
print("------------")

# Declarar el tipo de dato está de más
edad:int = fake.random_int(min=18, max=65)
#print('Edad: ' + edad.__str__())
print('Edad: ' + str(edad))

# Declarar el tipo de dato está de más
nombre:str = fake.name()
print('Nombre: ' + nombre)

# Declarar el tipo de dato está de más
direccion:str = fake.address()
print('Dirección: ' + direccion)

# Declarar el tipo de dato está de más
telefono:str = fake.phone_number()
print('Teléfono: ' + telefono)

# Declarar el tipo de dato está de más
correo:str = fake.email()
print('Correo: ' + correo)

# Declarar el tipo de dato está de más
fecha_nacimiento:str = fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d')
print('Fecha de nacimiento: ' + fecha_nacimiento)
