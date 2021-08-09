creditos = {"Matematicas" : 6, "Fisica" : 2, "Quimica" : 4} 
total_cred = 0

for materia, credito in creditos.items():
    print (f"{materia} tiene {creditos} creditos")
    total_cred += credito
print (f"El total de creditos es {total_cred}")


for materia in creditos:
    print (f"{materia} tiene {creditos[materia]} creditos")