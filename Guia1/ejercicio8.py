monto = float(input("Ingrese el monto que desea invertir "))
interes = float(input("Ingrese el interes anual "))
anos = int(input("Ingrese cantidad de años "))
for i in range (anos):
    monto += (monto*interes)/100
print (f"El monto obtenido seria de {monto} ")



#ESTE ESTA MAL