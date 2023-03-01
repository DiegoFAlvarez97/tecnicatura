class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decorador
    def nombre(self):  # Metodo Getter
        print('Estamos usando el metodo Get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo Setter
        print('Estamos usando el metodo Set')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2('Diego', 'Alvarez', 44)
    print(persona1.nombre)  # Llamamos al metodo Getter
    persona1.nombre = 'Juan Pedro'  # Llamamos al Setter
    print(persona1.nombre)  # Otra vez al metodo getter
    print(persona1.mostrar_detalle())  # Llamamos el metodo mostrar detalles
    # Atributo read-only seria la edad por que no tiene el metodo set
    print(persona1.edad)

    # Tarea crear 3 objetos mas, utilizando los metodos getter and setter
    # para modificar, y mostrar los cambios

    persona2 = Persona2('Florencia', 'Romero', 23)
    persona2.nombre = 'Florencia'
    persona2.apellido = 'Romero'
    persona2.edad = 23
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    print(persona2.mostrar_detalle())

    persona3 = Persona2('Carolina', 'Felisa', 21)
    persona3.nombre = 'Carolina'
    persona3.apellido = 'Felisa'
    persona3.edad = 21
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    print(persona3.mostrar_detalle())

    persona4 = Persona2('Natalia', 'Lucrecia', 56)
    persona4.nombre = 'Natalia'
    persona4.apellido = 'Lucrecia'
    persona4.edad = 56
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    print(persona4.mostrar_detalle())

    print(__name__)
