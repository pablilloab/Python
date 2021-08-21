def palabras (*pals):
    cant_letras=0
    palabra_mas_larga = []
    for palabra in pals:
        cant_caract = len(palabra)
        if cant_caract >= cant_letras:
            cant_letras = cant_caract
            palabra_mas_larga.append(palabra)
        
    print (f"Las palabras mas largas son {palabra_mas_larga} y tienen letras {cant_letras}")


palabras ("hhhhh", "asd", "yyyyy","Polo","ppppp")