# Ejercicio 8: Menu iteractivo - Cajero automatico
# Hacer un programa que simule un cajero automatico con un saldo
# Inicial de $1000 y tendra el siguiente menu de opciones:
#               1. Ingresar dinero en la cuenta
#               2. Retirar dinero de la cuenta
#               3. Mostrar dinero
#               4. Salir
saldo = 1000
while True:
    print("\t .:MENU:.")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero")
    print("4. Salir")
    opcion = int(input("Digite una opcion de menu: "))
    print()
    if opcion == 1:
        extra = float(input("Cuanto dinero desea ingresar -> "))
        saldo += extra
        print(f"Dinero en la cuenta ${saldo}")
    elif opcion == 2:
        print(f'Saldo disponible {saldo}')
        retirar = float(input("Digite cuanto dinero desea retirar de la cuenta: "))
        if retirar > saldo:
            print("No disponible la cantidad a retirar")
        else:
            saldo -= retirar
            print(f"Usted a retirado {retirar} su saldo es de {saldo}")
    elif opcion == 3:
        print(f"Su saldo es de {saldo}")
    elif opcion == 4:
        print("Hasta Luego")
        break