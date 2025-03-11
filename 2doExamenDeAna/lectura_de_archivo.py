# Ejemplo de lectura de un archivo de texto

def leer_archivo(nombre_archivo):
  """Lee el contenido de un archivo de texto.

  Args:
    nombre_archivo: El nombre del archivo a leer.

  Returns:
    El contenido del archivo como una cadena, o None si ocurre un error.
  """
  try:
    with open(nombre_archivo, 'r') as archivo:
      contenido = archivo.read()
    return contenido
  except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")
    return None
  except Exception as e:
    print(f"Error al leer el archivo: {e}")
    return None

# Ejemplo de uso
contenido_leido = leer_archivo("mi_archivo.txt")
if contenido_leido:
  print("Contenido del archivo:")
  print(contenido_leido)
  