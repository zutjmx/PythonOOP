# Se importa Faker
from faker import Faker
fake = Faker('es_MX')

# Se imprime un ciclo de nombres
print("============ Lista de Nombres ============")
for _ in range(10):
    print(fake.name().upper())
