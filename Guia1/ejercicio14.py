score = float(input("Ingrese la puntuacion del empleado "))
premio = 100000
if score == 0.0:
    print(f"Rendimiento inaceptable, recibirá {premio * 0.0}")
elif score == 0.4:
    print(f"Rendimiento aceptable, recibira {premio * 0.4}")
elif score >= 0.6:
    print(f"Rendimiento meritorio, recibira {premio * score}")