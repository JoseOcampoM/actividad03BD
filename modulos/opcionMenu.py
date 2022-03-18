import os, time, sys

list_empleados = []


class Persona:
    def __init__(self, nombre, direccion, telefono, cedula):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.cedula = cedula


class Empleado(Persona):
    def __init__(self, nombre, direccion, telefono, cedula, sueldo):
        Persona.__init__(self, nombre, direccion, telefono, cedula)
        self.sueldo = sueldo


def adicionar_empleado():
    s = 0
    while (s == 0):
        os.system('clear')
        nombre = input("Digite el nombre del empleado ==> ")
        direccion = input("Digite la direccion ==> ")
        telefono = input("Digite el telefono ==> ")
        cedula = input("Digite la cedula ==> ")
        sueldo = input("Digite el sueldo ==> ")

        emp = Empleado(nombre, direccion, telefono, cedula, sueldo)
        list_empleados.append(emp)

        print(""" 
        
        """)
        opc = str(input("Desea agregar otro empleado? (s/n) ==> "))
        if(opc == 's'):
            s = 0
        else: 
            s = 1

def salir():
    os.system('clear')
    print("Gracias por usar este servicio")
    time.sleep(1)
    sys.exit(0)
    
def eliminar_empleado():
    os.system('clear')
    c = input("Digite la cedula del Empleado ==> ") 

    for i in range(len(list_empleados)):
        if list_empleados[i].cedula == c:
            list_empleados.pop(i) 

def mostrar_empleado():
    os.system('clear')
    for empleado in list_empleados:
            print(f"{empleado.nombre} - {empleado.direccion} - {empleado.telefono} - {empleado.cedula} - {empleado.sueldo}")
    key=input("Presione cualquier tecla para continuar.")
