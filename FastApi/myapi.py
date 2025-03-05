from fastapi import FastAPI

from faker import Faker
fake = Faker('es_MX')

app = FastAPI()

@app.get("/")
def read_root():
    return {
                "nombre": fake.name(),
                "edad": fake.random_int(min=18, max=99),
                "email": fake.email(),
                "telefono": fake.phone_number(),
                "direccion": fake.address(),
                "fecha_nacimiento": fake.date_of_birth(),
                "status": fake.random_element(elements=('Activo', 'Inactivo'))
            }
