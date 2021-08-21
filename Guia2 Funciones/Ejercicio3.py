def bisiesto ():
    anio = int(input("Ingrese el año para calcular si es bisiesto "))
    if anio >= 0:
        if anio % 4 == 0:
            if not anio % 100 == 0:
                print ("Es bisiesto")
            elif anio % 400 == 0:
                print ("Es bisiesto")
            else:
                print ("No es bisiesto")
        else:
            print ("No es bisiesto")
    else:
        print ("No ingreso un año correcto ")

bisiesto()