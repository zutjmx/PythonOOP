# Se importa Faker
from faker import Faker
fake = Faker('es_MX')

# Se crea una lista vacía
lista = []
# Se crea un ciclo for para generar 10 datos
for i in range(10):
    # Se generan los datos
    nombre = fake.name()
    edad = fake.random_int(18, 80)
    email = fake.email()
    # Se añaden los datos a la lista
    lista.append({'nombre': nombre, 'edad': edad, 'email': email})

# Se imprime la lista
print(lista)

primer_numero = fake.random_int(1, 10)
segundo_numero = fake.random_int(1, 10)

print("Primer número: ")
print(primer_numero)

print("Segundo número: ")
print(segundo_numero)
