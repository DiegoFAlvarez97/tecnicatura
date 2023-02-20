from Persona2 import Persona2
print('Creacion de objetos'.center(30, '-'))

if __name__ == '__main__':
    persona5 = Persona2('Lionel', 'Messi', 35)
    persona5.mostrar_detalle()

    print(__name__)

print('Eliminacion de Objetos'.center(30, '-'))
del persona5