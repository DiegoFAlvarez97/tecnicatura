from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    #print(objeto) #De manera indirecta llama al str de la clase Empleado
    print(type(objeto)) # Esto es para saber el tipo de dato que recibe
    print(objeto.mostrar_detalle())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)



empleado = Empleado('Diego', 60000)
imprimir_detalles(empleado)

gerente = Gerente('Tatitana', 70000, 'Sistemas')
imprimir_detalles(gerente)
