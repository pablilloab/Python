def rectangulo (caracter="*"):
    base = int(input("Ingrese la base del rectangulo "))
    altura = int(input("Ingrese la altura del rectangulo "))
    for i in range (altura):
        print (base * caracter)
rectangulo()

