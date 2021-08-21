def rectangulo ():
    base = int(input("Ingrese la base del rectangulo "))
    altura = int(input("Ingrese la altura del rectangulo "))
    caracter = input("Ingrese el caracter para dibujar ")
    for i in range (altura):
        print (base * caracter)

rectangulo ()