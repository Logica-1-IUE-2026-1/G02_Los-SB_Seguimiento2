""" Este codigo es para validar el acceso a una discoteca,
 pregunta la edad y el sexo de la persona, si cumple las condiciones
 arroja el mensaje "acceso permitido", 
 si no cumple con las condiciones el mesnaje será "acceso denegado". """

edad = int(input("ingrese su edad: "))

if edad >= 18:
    print("acceso permitido")

    sexo = int(input("ingrese el sexo: "))
    if sexo == "femenino":
        print("acceso permitido")
    else:
        print("acceso denegado")
else:
    print("acceso denegado")
