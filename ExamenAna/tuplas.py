# Las tuplas son estructuras de datos en Python 
# que permiten almacenar múltiples elementos en un solo objeto. 
# Las tuplas son inmutables, 
# lo que significa que no pueden ser modificadas después de su creación. 
# Aquí tienes un ejemplo básico de cómo crear y utilizar tuplas en Python:

# Crear una tupla
mi_tupla = (1, 2, 3, "a", "b", "c")

# Acceder a elementos de la tupla
primer_elemento = mi_tupla[0]
ultimo_elemento = mi_tupla[-1]

# Imprimir los elementos
print(f"Primer elemento: {primer_elemento}")
print(f"Último elemento: {ultimo_elemento}")

# Desempaquetar una tupla
a, b, c, d, e, f = mi_tupla
print(f"Desempaquetados: {a}, {b}, {c}, {d}, {e}, {f}")

# Intentar modificar un elemento (esto provocará un error)
# mi_tupla[0] = 10  # Descomenta esta línea para ver el error
