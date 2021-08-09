frase = input("Ingrese su frase: ")
letra = input("Ingrese la letra a buscar repeticiones ")
repeticiones = 0
for i in range (len(frase)):
    if frase[i] == letra:
        repeticiones += 1
print (f"La letra ingresada se repite {repeticiones} veces")


for caracter in frase:
    if caracter == letra:
        repeticiones +=1


#repeticiones = frase.count(letra)