class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar (self):
        return f"""Nombre: {self.nombre}
        Edad: {self.edad}
        DNI: {self.dni}"""

    def esMayorEdad (self):
        if self.edad > 18:
            return True
        else:
            return False

class cuenta:
    def __init__ (self, titular=Persona(), cantidad=0.0): #Herencia indirecta por el atrubuto titular
        self.titular = titular
        self.cantidad = cantidad

    def mostrar (self):
        print (self.titular.mostrar())
        print (f"Cantidad --> {self.cantidad}")

    def ingresar (self, montoIngresado):
        if montoIngresado >= 0:
            self.cantidad += montoIngresado

    def retirar (self, montoRetirar):
        self.cantidad -= montoRetirar

pablo = Persona ("Pablo", 38, "29832537")
print(pablo.esMayorEdad())

cuenta1 = cuenta(pablo, 10000)
cuenta1.mostrar()


class CuentaJoven (cuenta):
    def __init__ (self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    def esTitularValido (self):
        if self.titular.esMayorEdad() and self.titular.edad < 25:
            return True
        else:
            return False

    def retirar (self, montor):
        if self.esTitularValido():
            self.cantidad -= montor
            print (f"Saldo disponible {self.cantidad}")
        else:
            print("No es titular valido de cuenta joven")

    def mostrar (self):
        print ("Cuenta Joven")
        print (f"Bonificacion --> {self.bonificacion}%")
