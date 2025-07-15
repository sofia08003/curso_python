#Usando title().
#Pregunta al usuario por su nombre
nombre=input("¿cual es tu nombre? ")
#strip elimina espacios en blanco
nombre= nombre.strip()
#capitalizar.
nombre=nombre.title()
#Imprime hola mas el nombre ingresado
print(f"hola, {nombre}")
