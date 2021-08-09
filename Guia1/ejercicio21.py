asignatura = input ("Escriba su asignatura o salir para terminar: ")
list_asig = []
while asignatura != "salir":
    list_asig.append(asignatura)
    asignatura = input ("Escriba su asignatura o salir para terminar: ")
for i in range(len(list_asig)):
    print(f"Yo estudio {list_asig[i]}")
