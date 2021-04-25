class Menu_Principal:

    def primeraVista(self):
        print("Bienvenido al menu principal")
        valores = {"1 - Programa de Flujo de Dinero": 1, "2 - Crear/Guardar tareas": 2}
        for i in valores:
            print (i)

class Opciones:
    def __init__(self,valor):
        self.valor = valor

    def getValor(self):
        return self.valor
    
    def opciones(self):
        if(self.getValor() == 1):
            print("Bienvenido a POO" + "\nPerfecto empecemos con el control de flujo de dinero")
            print("+ Ingresar: ")
            print("- Gasto: ")

ingresos = []
gastos = []

class PrimerPrograma:
    def __init__(self,ingreso,gasto):
        self.ingreso = ingreso
        self.gasto = gasto

    def getIngreso(self):
        return self.ingreso
    def getGasto(self):
        return self.gasto
    
    def addIngreso(self):
        if(self.getIngreso() == "Ingresar"):
            opc1=input("Cuantos ingresos tuviste hoy: ")
            for i in range(opc1):
                ingresosHoy = input("Ingreso " + str(i+1) + ": $ ")
                ingresos.append(ingresosHoy)
            return ingresos
            
    def addGasto(self):    
        if(self.getGasto() == "Gasto"):
            opc2=input("Cuanto gastaste hoy: ")
            for i in range(opc2):
                gastosHoy = input("Gasto N " +str(i+1) + ": $ ")
                gastos.append(gastosHoy)
            return gastos