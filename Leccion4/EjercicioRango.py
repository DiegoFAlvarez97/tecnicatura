'''
Sintaxis de range(inicio<opcional>, fin <requerido>, incremento <opcional>)

Ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
Ejemplo de ejecucion: 3, 5, 7, 9

'''
# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numerod divisibles entre 3
# Ejemplo de ejecucion: 0, 3, 6, 9
print('Rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)


#Ejercicio 2: Crear un rango de numeros de 2 a 6 imprimelos
# Ejemplo de ejecucion: 2,3,4,5,6

print("Rango de numeros de  2 a 6")
for i in range(2,7):
    print(i)

#Ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
#Ejemplo de ejecucion: 3, 5, 7, 9

print("Rango de valores de inicio = 3, fin = 10, incremento = 2")
for i in range(3, 11, 2):
    print(i)

#Definimos una tupla
cocina = ('Cuchara', 'Cuchillo', 'Tenedor')
print(len(cocina))

#Accedemos a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:1])
# Ejemplo
verduras = ('papa',) # Si o si necesita la coma para que sea una tupla
# de lo contradiro solo seria un tipo string

# Recorremos el elemento de la tupla
for cocinar in cocina:# Print esta usando \n  para saltos de lineas
    print(cocinar, end=' ') # Usanmos end para eliminar los saltos de linea

cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

# del cocina elimina la tupla
print(cocina)




