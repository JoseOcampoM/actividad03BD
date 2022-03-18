from modulos.menu import mostrarMenu
from modulos.opcionMenu import *


eleccion={
    "1":adicionar_empleado,
    "2":eliminar_empleado,
    "3":mostrar_empleado,
    "4":salir
}

def run():
    while True:
        mostrarMenu()
        opc=input("Digita la opción==> ")
        accion=eleccion.get(opc)
        if accion:
            accion()
        else:
            print("La opcion no es valida...")
			
			
def main():
    run()

if __name__ == '__main__':
    main()