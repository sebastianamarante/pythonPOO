from menuPO import *

def pantallaInicial():
    menuPrincipal = Menu_Principal()
    menuPrincipal.primeraVista()
    valor = input('Que desea hacer hoy: ')
    opcs = Opciones(valor)
    opcs.opciones()
    opciones = raw_input()
    return opciones

opciones = pantallaInicial()
print(opciones)

while(opciones == "Ingresar"):
    if (opciones == "Ingresar"):
        ingreso = opciones
        gasto = opciones
        primerPrograma= PrimerPrograma(ingreso,gasto)
        totalIngresos = primerPrograma.addIngreso()
        sumaDeIngresos = str(sum(totalIngresos))
        print("Bien! Hoy vas ganando: $" + sumaDeIngresos + "\n Presione 0 Si desea volver al Menu")
        print(totalIngresos)
        back = input()
        if (back == 0):
            opciones = pantallaInicial()
        else:
            print("Muchas gracias por utilizar nuestro software.")
            break

while (opciones == "Gasto"):
    if (opciones == "Gasto"):
        ingreso = opciones
        gasto = opciones
        primerPrograma= PrimerPrograma(ingreso,gasto)
        totalGastos = primerPrograma.addGasto()
        sumaDeGastos = str(sum(totalGastos))
        print("Hoy vas gastando: " + sumaDeGastos + "\n Presione 0 Si desea volver al Menu")
        print(totalGastos)
        back = input()
        if (back == 0):
            opciones = pantallaInicial()
        else:
            print("Muchas gracias por utilizar nuestro software.")
            break