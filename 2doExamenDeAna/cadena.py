# Aquí tienes un ejemplo de código en Python que demuestra diversas operaciones comunes en el manejo de cadenas. 
# Este script abarca desde la eliminación de espacios, 
# conversión de mayúsculas/minúsculas, 
# división en palabras, 
# concatenación, 
# formateo, 
# reemplazo de subcadenas, 
# búsqueda y extracción (slicing) de partes de la cadena.

# Ejemplo de manejo de cadenas en Python

# Cadena original con espacios adicionales
cadena = "   Hola, esto es un ejemplo de manejo de cadenas en Python.   "

# 0. Cadena original
print("Cadena original:", cadena)

# 1. Eliminación de espacios en blanco al inicio y al final
cadena_limpia = cadena.strip()
print("Cadena sin espacios:", cadena_limpia)

# 2. Conversión a mayúsculas y minúsculas
print("Mayúsculas:", cadena_limpia.upper())
print("Minúsculas:", cadena_limpia.lower())

# 3. División de la cadena en palabras (crea una lista)
palabras = cadena_limpia.split()
print("Lista de palabras:", palabras)

# 4. Concatenación de cadenas
saludo = "¡Hola"
nombre = "Mundo"
mensaje = saludo + ", " + nombre + "!"
print("Mensaje concatenado:", mensaje)

# 5. Uso de f-strings para formatear cadenas
edad = 25
presentacion = f"Mi nombre es {nombre} y tengo {edad} años."
print("Presentación con f-string:", presentacion)

# 6. Reemplazar una subcadena por otra
cadena_modificada = cadena_limpia.replace("ejemplo", "demo")
print("Cadena modificada:", cadena_modificada)

# 7. Buscar la posición de una subcadena específica
posicion = cadena_limpia.find("manejo")
print("La posición de 'manejo' es:", posicion)

# 8. Acceso a subcadenas (slicing)
subcadena = cadena_limpia[7:20]
print("Subcadena (slicing):", subcadena)

# 9. Longitud de la cadena
longitud = len(cadena_limpia)
print("Longitud de la cadena:", longitud)

# 10. Verificar si una cadena comienza o termina con una subcadena específica
comienza_con = cadena_limpia.startswith("Hola")
termina_con = cadena_limpia.endswith("Python.")
print("Comienza con 'Hola':", comienza_con)
print("Termina con 'Python.':", termina_con)

# 11. Contar la cantidad de veces que aparece una subcadena
cantidad = cadena_limpia.count("o")
print("Cantidad de 'o':", cantidad)
