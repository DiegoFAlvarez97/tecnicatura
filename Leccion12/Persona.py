class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} + {other.nombre}'

    def __sub__(self, otro):
        return self.edad - otro.edad

persona1 = Persona('Diego', 77)
persona2 = Persona('Rafael', 88)

# persona1.__add__(persona2) Sintaxis interna automaticaa

print(persona1 + persona2)
print(persona1 - persona2)