# Lista = Diego, Fernando, Natalia, Osvaldo

lista = ['Diego', 'Fernando', 'Natalia', 'Celes']
print(lista)
print(lista[0])
print(lista[1])
print(lista[3])
print(lista[-1])
print(lista[-2])

print(lista[0:2])# Solo muestra del indice 0 al 1, pero no el 2
# Ir del inicio de la lista al indice (sin incluirlo)

print(lista[ :3])# Indices a mostrar 0, 1, 2
#Desde el indice indicado hasta el final
print(lista[1: ])
# Modificamos un valor de nuestra lista
lista[3] = 'Liliana'
lista[0] = 'Ariel'
print(lista)
# Iterar lista
for nombre in lista:
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene
print(len(lista)) #Pasamos como parametro lista

#agregamos un elemento
lista.append('Marcelo')
lista.append([1, 2, 3])
lista.append(True)
lista.append(10.44)
lista.append([4, 5])
lista.append(7)

print(lista)

# Insertar un elemento en un indice especifico
lista.insert(1, 'Carlos')
print(lista)
lista.insert(3, 'Domingo')
print(lista)

#Eliminamos un elemento de nuestra lista
lista.remove('Carlos')
print(lista)

#Eliminar el ultimo elemento
lista.pop()
print(lista)

# Eliminar un indice especifico
del lista[2] # del significa delete eliminar
print(lista)

# Borrar todos los elementos de la lista
lista.clear()
print(lista)

#del lista
print(lista)



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

# Tipo set
planetas = {'Marte', 'Saturno', 'Venus'}
print(len(planetas))

# revisasmos si un elemento existe dentro del set
print('Marte' in planetas)

#Agregar un elemento
planetas.add('Tierra') # add es una funcion
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Marte')# Esta funcion ante un mal ingreso u inexistencia
print(planetas)
print(planetas)
planetas.discard('Saturno') # Esta funcion no nos representa ningun error

# 'Maradone':10  Un dicccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key, value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos'
}
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave (key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entonrno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)

# Necesitamos una funciono para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():# Estamos usando una funcion
    print(termino) # Muestra solo las llaves

for valor in diccionario.values(): # Usamos una funcion para acceder al valor
    print(valor)

# Comprobar la existencia de algun elemento
print('IDE' in diccionario) # Devuelve un booleano

# Agregar un elemento a nuestro diccionario
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario # El diccionario se BORRRO

# Concatenacion de Listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2 # Concatenamos
print(lista3)

lista3.extend([7, 8, 9, 1]) # Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Funcion para ubicar en que indice esta el valor ingresado
# print(lista3.index(0)) # esto dara un error por no ser el elemento parte de la lista

# Como saber cuantos elementos repetidos hay dentro en una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de una lista

# Para poner al revez una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista4 = [1, 2, 3] * 3
print(lista4)

lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento, en python es una funcion
lista3.sort() # Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True)
print(lista3)

tupla = (4, 'Hola', 4.75, [1, 3, 18], 4, 'Como estas?') # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

# Repaso de set o conjunto
# para definir un conjunto
conjunto = set()
conjunto1 = {'bye',}
conjunto.add(7)
conjunto.add('Hola')
print(conjunto)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el numero 3 NO esta en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto) # Nos deuelve la respuesta como Booleano


# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto # La linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto & conjunto1 # Que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto # Asigna el valor que esta en el conjunto1 y no en el conjunto
print(conjunto3)
conjunto3 = conjunto - conjunto1
print(conjunto3)
conjunto3 = conjunto ^ conjunto1 # Elementos que no comparten o que son diferentes enetre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto
print(conjunto.issubset(conjunto3)) # Aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto))
print(conjunto3.issubset(conjunto1))

print(conjunto3.issubset(conjunto1)) # Preguntamos si los elementos del conjunto estan dentro del 3
print(conjunto3.issubset(conjunto)) # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto1.issubset(conjunto3))

# Como saber si ambos conjuntos son disconexsos, esto es si no comparten elementos en comun
print(conjunto.isdisjoint(conjunto1))

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutble
# No se puede agregar, modificar ni eliminar elementos del conjunto


# Repaso de Diccionarios
DiccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(DiccionarioNuevo)

# Como eliminar
del (DiccionarioNuevo['Azul'])
print(DiccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Diego': {'edad': 25, 'Altura': 1.78}, 'Rosado': [54, 1.77], 'Celeste': [13, 1.63]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura':1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura':1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    21: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura':1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura':1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensor Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura':1.83, 'Precio': '3.5 Milones', 'Posicion': 'Arquero'}
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)

print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() # Quita el ultimo elemento y lo guarda en la variable
print(f' Sacamos el elemento {elementoBorrado}')
print(f' La pila ahora se quedo asi: {pila}')

# Colas con lista
# Estructura de datos de tipo fifo(first input / first output)
cola = ['Diego', 'Celeste', 'Maria', 'Lautaro']

# Agregamos elemento al final de la cola
cola.append('Fernando')
cola.append('Jose')
print(cola)

# Sacamos elementos de cola
seRetira = cola.pop(0)
print(f'Atiendido {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atiendido {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atiendido {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atiendido {seRetira}')
print(cola)

# Seguimos mostrando como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')