def hola():

    print("hola")
#pedir nombre.    
nombre= input("nombre: ")
#llamando la funcion.
hola()
print(nombre) 


#mejorando el codigo:
def hola(para):

    print("hola", para)
#pedir nombre.    
nombre= input("¿cual es tu nombre?")
#llamando la funcion.
hola(nombre) 


#con main:
def main():
    nombre= input("¿cual es tu nombre?").strip().title()
    hola(nombre)
    hola()
def hola(para="mundo"):
    print("hola",para)
main()

#con enteros:
def main():
    x=int(input("¿cual es x?"))
    print("x el cuadrado es:" , cuadrado(x))
def cuadrado(n):
    resultado= n*n
    return resultado
main()