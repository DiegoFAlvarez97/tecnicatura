# Ejercicio 3: Funcion Recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funciones rescursivas
# Puede ser cualquier valor positivo, por ejemplo, si le pasamos el
# valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser el numero 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan numeros negativos no imprime nada
def imprimir_numeros_recursivos(numero):
    if numero >= 1: # Caso Base
        print(numero)
        imprimir_numeros_recursivos(numero-1) # Caso Recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print("El valor ingresado no es valido")

imprimir_numeros_recursivos(5)