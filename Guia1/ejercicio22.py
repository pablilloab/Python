frutas = {
    "Banana": 80 ,
    "Manzana": 100,
    "Pera": 120,
    "Naranja": 150
}

fruta = input ("Ingrese una fruta ").capitalize() #conviete la primera letra en mayusculas y el resto en minusculas


if fruta in frutas:
    kilos = float (input("Ingrese la cantidad de kilos "))
    precio = kilos * frutas [fruta]
    print(f"El precio de {fruta} es {precio} pesos")
else:
    print ("No ingreso una fruta de la lista ")
