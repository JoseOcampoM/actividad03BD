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

    

