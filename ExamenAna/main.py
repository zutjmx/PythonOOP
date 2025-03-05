cantidad = -1
while cantidad <= 0:
    cantidad = int(input("Ingrese la cantidad de numeros que desea ingresar: "))
    if cantidad > 0:
        break
print("Cantidad registrada: ", cantidad)

productos = ["pantalon","Camisa","Zapatos","Corbata","Chaqueta"]
for producto in productos:
    print(producto)

intentos = 1
while intentos < 4:
    password = input("Ingrese su password: ")
    if password == "1234":
        print("Acceso permitido")        
    intentos += 1

print("Acceso denegado")

for intentos in range(3):
    password = input("Ingrese su password: ")
    if password == "1234":
        print("Acceso permitido")
        break
else:
    print("Acceso denegado")

productos = ["pantalon","Camisa","Zapatos","Corbata","Chaqueta"]
for i in range(len(productos)):
    print(productos[i])
