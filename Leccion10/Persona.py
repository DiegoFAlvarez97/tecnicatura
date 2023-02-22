class Persona:
    contador_personas = 0 # Variable de clase

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1 # vamos incrementando
        return cls.contador_personas

    def __init__(self, nombre, edad):
        Persona.contador_personas += 1 # vamos incrementando
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad} ]'

persona1 = Persona('Diego', 25)
print(persona1)
persona2 = Persona('Arnolo', 32)
print(persona2)
persona3 = Persona('Anacleta', 23)
print(persona3)
Persona.generar_siguiente_valor()
Persona4 = Persona('Natalia', 19)
print(Persona4)
print(f'Valor contador personas: {Persona.contador_personas}')