# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion
# Elimine los elementos repetidos, por ultimo mostrar la lista.

# Creamos una lista
lista = [1, 2, 3, 'Diego', 7, 7, 3, 'Charly', 4, 'Beta']
#conjunto = set(lista) # Convertimos la lista en un conjunto de tipo set
#lista = list(conjunto) # Convertimos el conjunto a una lista
lista = list(set(lista)) # La conversion hecha en una sola linea de codigo (eficiente)
print(lista)
