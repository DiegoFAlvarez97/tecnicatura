class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Se lo llama metodo Init Dunder
        self.__nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): # self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.__nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}')


persona1 = Persona("Diego", "Alvarez", 25)  # Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
print(f'El objeto de la clase persona {persona1.nombre} {persona1.apellido} su edad es de : {persona1.edad}')

persona2 = Persona('Daniel', 'Angel', 2315673589 ,46)
print(f'El objeto de la clase persona {persona2.nombre} {persona2.apellido} su edad es de : {persona2.edad}')

persona1.nombre = "Liliana"
persona1.apellido = "Roadmindia"
persona1.edad = 30
print(f'El objeto de la clase persona {persona1.nombre} {persona1.apellido} su edad es de : {persona1.edad}')

# Los atributos son: caracteristicas
# Los metodos son: el comportamiento que van a tener los onjetos (acciones)
persona1.mostrar_detalle()# La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

#Persona.mostrar_detalle() # Debemos pasarle una referencia para el self o dara error
persona1.telefono = '43335123'
print(f'Este es el telefono de {persona1.nombre} {persona1.telefono}') # Hemos creado un atributo de un onjeto

#print(persona2.telefono) el objeto persona2 no tiene ese atributo, da error
persona3 = Persona('Rogelio', 'Buendia', 21412518, 27, 'Telefono', '1231212251251','Calle Lopez' , 859, 'Manzana', 77, 'Casa', 19, altura=1.86, CFavorito='Azul', Auto='Citroen', Modelo=2021)
persona3.mostrar_detalle()
#print(persona3._dni) #Esto no se debe utilizar( esta encapsulado), esto dice que lo desconocemos python
# persona.__nombre # Esta totalmente encapsulado