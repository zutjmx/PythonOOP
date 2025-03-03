# Manejar excepciones en Python es esencial para escribir código robusto y evitar errores 
# inesperados durante la ejecución del programa. 
# Aquí tienes un ejemplo básico de cómo manejar excepciones usando bloques try, except, 
# y opcionalmente else y finally:

def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None
    except TypeError:
        print("Error: Ambos argumentos deben ser números.")
        return None
    else:
        print("División exitosa.")
        return resultado
    finally:
        print("Operación de división completada.")

# Llamar a la función con diferentes casos
print(dividir(10, 2))   # División válida
print(dividir(10, 0))   # Error: División entre cero
print(dividir(10, "a")) # Error: Tipo de datos incorrecto
