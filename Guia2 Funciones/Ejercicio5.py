def generador_listas ():
    print ("Generador de listas ")
    cant_listas = int (input ("Cuantas listas desea crear "))
    for i in range (1, cant_listas + 1):
        lista_palabras =[]
        cant_palabras = int(input(f"Ingrese la cnatidad de palabras de la lista {i}"))
        for j in range (cant_palabras):
            palabra = input("Ingrese una palabra ")
            lista_palabras.append(palabra)
        print (f"Lista {i}: {lista_palabras}")

generador_listas()
        