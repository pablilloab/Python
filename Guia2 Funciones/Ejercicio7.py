import random
def juego ():
    numero = random.randint (0, 1000)
    numero_us = int (input("Ingrese un numero entero entre 0 y 1000: "))
    intento = 1
    while intento < 7:
        if numero > numero_us:
            print ("Es mas alto")
            numero_us = int (input("Ingrese un numero entero entre 0 y 1000: "))
        elif numero < numero_us:
            print ("Es mas bajo")
            numero_us = int (input("Ingrese un numero entero entre 0 y 1000: "))
        else:
            print ("Viva Python")
            break
        intento +=1
    else:
        print ("Alpiste perdiste")


juego ()