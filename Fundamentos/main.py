import util

if __name__ == '__main__':
    print('Se va a invocar la función decirHola')   
    util.decirHola('Jesús Zúñiga Trejo')
        
nombre = util.generarNombre()
email = util.generarEmail()
direccion = util.generarDireccion()
telefono = util.generarTelefono()

print('Se van a imprimir datos falsos generados por Faker')
print(nombre)
print(email)
print(direccion)
print(telefono)
