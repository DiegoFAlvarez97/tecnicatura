# Comenzamos Funciones
# mi_funcion() No se puede llamar antes de definir una funcion
# Definimos una funcion
def mi_funcion():# Para identificar a la funcion utiizamos parentecis
    print('Saludos a todos')

mi_funcion()#Estamos llamando a la funcion
mi_funcion()# Se puede llamar a la funcion N cantidad de veces

# Desempaquetado de lista o list Unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ["Diego", "Alvarez"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*person) # Estos es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Fernando", "Fregenal") # desempaquetamos a travez de una tupla
show(*person2)
person3 = {"lastName": "Fregenal", "name": "Diego"}
show(**person3)

numbers = [1, 2, 3, 4, 5] # Aun con una lista vacia se ejecuta el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print('Esto se termina')

# List comprehension, lista de comprencion
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'P'] # Esto regresa una nueva lista
print(alongP)

bottleC = [{"name":"Quilmes", "contry":"Arg"},
           {"name":"Corona", "contry":"Mx"},
           {"name":"Stella Artois", "contry": "Belgium"}
           ]
Arg = [b for b in bottleC if b["contry"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos")
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion2('Diego', 'Alvarez')
mi_funcion2('Anabel', 'Rodriguez')

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a, b):
    return a + b
# resultado = sumar(44, 21)
# print(f'La suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 12)}')

def sumar2(a = 0, b = 0) -> int: # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# Argumentos variables en funciones
def listaNombres(*nombres): #Normalmente se utiliza: *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listaNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'Maria')
listaNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')