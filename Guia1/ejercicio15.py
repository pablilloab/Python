edad = int(input("Ingrese la edad del cliente: "))
if edad < 4:
    print("Cliente menor de edad, entrada sin costo")
elif edad >= 4 and edad <= 18:
    print("El costo de la entrada es de $500")
else:
    print("El costo de la entrada es de $1000")