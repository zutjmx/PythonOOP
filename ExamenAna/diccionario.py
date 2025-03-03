# Los diccionarios son estructuras de datos que almacenan pares de clave-valor, 
# lo que permite acceder a los valores utilizando sus claves correspondientes.

# Crear un diccionario
mi_diccionario = {
    "nombre": "Ana",
    "edad": 52,
    "ciudad": "Ciudad de México"
}

# Acceder a los valores del diccionario usando las claves
nombre = mi_diccionario["nombre"]
edad = mi_diccionario["edad"]
ciudad = mi_diccionario["ciudad"]

# Imprimir los valores
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Ciudad: {ciudad}")

# Agregar un nuevo par clave-valor al diccionario
mi_diccionario["profesión"] = "Ingeniero"

# Modificar un valor existente
mi_diccionario["edad"] = 26

# Eliminar un par clave-valor
del mi_diccionario["ciudad"]

# Iterar sobre el diccionario e imprimir las claves y valores
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")
