class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, edad):  # Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona("Diego", "Alvarez", 25)  # Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
print(f'El objeto de la clase persona {persona1.nombre} {persona1.apellido} su edad es de : {persona1.edad}')

persona2 = Persona('Daniel', 'Angel', 46)
print(f'El objeto de la clase persona {persona2.nombre} {persona2.apellido} su edad es de : {persona2.edad}')

persona1.nombre = "Liliana"
persona1.apellido = "Roadmindia"
persona1.edad = 30
print(f'El objeto de la clase persona {persona1.nombre} {persona1.apellido} su edad es de : {persona1.edad}')

# Los atributos son: caracteristicas
# Los metodos son: el comportamiento que van a tener los onjetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()