# Se importa Faker
from faker import Faker
fake = Faker('es_MX')

numero_aleatorio = fake.random_int(min=10, max=25)
print("============ Número Aleatorio ============")
print(numero_aleatorio)

# Lllenar una lista con nombres de tamaño aleatorio
nombres = []
for _ in range(numero_aleatorio):
    nombres.append(fake.name())

# Se imprime la lista de nombres
print("============ Lista de Nombres ============") 
print(nombres)

# Lista vacía
lista_vacia = []
# Se imprime la lista vacía
print("============ Lista Vacía ============")
print(lista_vacia)

for _ in range(numero_aleatorio):
    lista_vacia.append(fake.address())

# Se imprime la lista de nombres
print("============ Lista de Direcciones ============")
print(lista_vacia)

direccion = lista_vacia[numero_aleatorio-1]
print("============ Dirección ============")
print(direccion)
