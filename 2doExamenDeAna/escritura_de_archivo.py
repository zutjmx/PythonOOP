# Escribe un programa que cree un archivo de texto y escriba en él una cadena de texto.

def escribir_archivo(nombre_archivo, contenido):
  """Escribe contenido en un archivo de texto.

  Args:
    nombre_archivo: El nombre del archivo a crear o sobrescribir.
    contenido: El texto a escribir en el archivo.
  """
  try:
    with open(nombre_archivo, 'w') as archivo:
      archivo.write(contenido)
    print(f"Se ha escrito el archivo '{nombre_archivo}' correctamente.")
  except Exception as e:
    print(f"Error al escribir el archivo: {e}")

# Ejemplo de uso
escribir_archivo("mi_archivo.txt", "Este es un ejemplo de contenido.")
