class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho alto y profundidad, con
    un metodo calcular_volumen que tendra la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores
    """

    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad

ancho = int(input("Digite el numero para el ancho del Cubo: "))
altura = int(input("Digite el numero para el alto del Cubo: "))
profundidad = int(input("Digitte el numero de la proundidad del Cubo "))
cubo1 = Cubo(ancho, altura, profundidad)
print(f'El volumen del cubo ingresado es: {cubo1.calcular_volumen()}')