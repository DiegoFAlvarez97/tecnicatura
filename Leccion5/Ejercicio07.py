# Ejercicio 7: Juego de adivina el numero
# Realizar un juego para adivinar un numero. Para ello se debe
# generar un numero aleatorio entre 1 - 100, y luego ir pidiendo numeros
# indicando 'es mayor' o 'es menor' segun sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y alli se debe mostrar el numero de intentos.
import random
aleatorio = random.randint(0, 100)# Toma de 0 a 100 literal, generamos un numero aleatorio
contador = 0
while True:
    numero = int(input("Digite un numero: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el numero, digita el numero menor")
    elif numero < aleatorio:
        print("\tNo es el numero, digite un numero mayor")
    else:
        print(f"Felicidades el numero {aleatorio} es el correcto has ganado el juego")
        print(f'Has encontrado el numero en {contador} cantidad de veces')
        break# Rompe el bucle