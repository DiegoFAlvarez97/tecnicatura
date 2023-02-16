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
planetas.discard('Saturno') # Esta funcion no nos representa ningun error
print(planetas)
