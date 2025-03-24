# Se importa Faker
from faker import Faker
fake = Faker('es_MX')

def decirHola(nombre):
    print(f'Hola {nombre}')
    #print('Hola {nombre}'.format(nombre=nombre))

def generarNombre():
    return fake.name()

def generarEmail():
    return fake.email()

def generarDireccion():
    return fake.address()

def generarTelefono():
    return fake.phone_number()

def generarCiudad():
    return fake.city()

def generarCodigoPostal():
    return fake.postcode()

def generarEstado():
    return fake.state()

def generarTexto():
    return fake.text()

def generarNumero():
    return fake.random_number()

def generarFecha():
    return fake.date()

def generarHora():
    return fake.time()
