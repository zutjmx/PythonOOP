# A continuación, te muestro un ejemplo completo que ilustra cómo escribir en un archivo y luego leerlo en Python. 
# Este código utiliza el manejador de contexto with, 
# lo que garantiza que el archivo se cierre correctamente después de realizar la operación.

# Ejemplo de lectura y escritura de archivos en Python

# 1. Escritura en un archivo
# Abrimos (o creamos) el archivo "ejemplo.txt" en modo escritura ("w")
with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
    # Definimos el contenido que deseamos escribir
    contenido = (
        "Este es un ejemplo de escritura en un archivo.\n"
        "Podemos escribir múltiples líneas de texto.\n"
        "La utilización de 'with' asegura que el archivo se cierre al finalizar.\n"
    )
    # Escribimos el contenido en el archivo
    archivo.write(contenido)

print("Se ha escrito en el archivo 'ejemplo.txt' exitosamente.")

# 2. Lectura completa del archivo
# Abrimos el archivo en modo lectura ("r")
with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    # Leemos todo el contenido del archivo
    contenido_leido = archivo.read()

print("Contenido leído del archivo:")
print(contenido_leido)

# 3. Lectura línea por línea
with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    print("Lectura línea por línea:")
    for linea in archivo:
        # Utilizamos strip() para eliminar el salto de línea al final de cada línea
        print(linea.strip())
