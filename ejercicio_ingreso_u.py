"""este codigo sirve para verificar el ingreso de estuduantes y docentes a la universidad"""
ROL = str(input("escriba en mayusculas el rol de la persona"))
if ROL == ("DOCENTE"):
    print ("ingreso permitido")
elif ROL == ("ESTUDIANTE"):
    print ("ingreso permitido")
else:
    print ("denegar ingreso")