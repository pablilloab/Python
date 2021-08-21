def bisiestos ():
    anio_1 = int(input("Ingrese el primer año "))
    anio_2 = int(input("Ingrese el segundo año "))
    cont = 0
    if (anio_1 >= 0 and anio_2 >=0 and anio_1 < anio_2):
        for i in range (anio_1, anio_2 + 1):
            if i % 4 ==0:
                if not i % 100 ==0:
                    cont +=1
                elif i % 400 == 0:
                    cont +=1
    elif anio_1 < 0 or anio_2 <0:
        print ("No ha infresado alos correctos ")
    elif anio_1 > anio_2:
        print ("El primer año deberia ser menor q el segundo")
    print (f"Entre {anio_1} y {anio_2} inclusive hubo {cont} años bisiestos")

    
bisiestos()