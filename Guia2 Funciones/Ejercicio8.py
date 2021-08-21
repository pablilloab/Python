def invertir(frase):
    frase = frase.split() #convierto en una lista la cadena de texto
    frase_reverse = []
    for palabra in frase:
        palabra = palabra [::-1] #slice, repasar
        frase_reverse.append(palabra)
    frase = " ".join(frase_reverse)
    print(frase)

invertir ("Lorem ipsum ist amet")