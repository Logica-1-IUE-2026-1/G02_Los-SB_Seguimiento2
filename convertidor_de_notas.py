""" Convertidor de notas.
    Este codigo tiene como función principal validar que letra le corresponde 
    como calificación a cada estudiante según el valor. """

nota = float(input("ingrese la nota actual del estudiante: "))

if nota >= 4.5:
    print("la calificación es: A")
elif nota >= 3.5:
    print("La calificación es: B")
elif nota >= 3:
    print("La calificación es: C")
elif nota >= 2:
    print("La calificación es: D")
else:
    print("La calificación es: E")
