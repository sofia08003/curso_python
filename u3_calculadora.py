#enteros(int).
x=int(input("¿cual es x?"))
y=int(input("¿cual es y?"))
z=x+y
print(z)
#float(valores decimales).
a=float(input("¿cual es a?"))
b=float(input("¿cual es b?"))
print(a+b)
#round(valores redondeados).
#obtiene entradas.
a=float(input("¿cual es a?"))
b=float(input("¿cual es b?"))
#redondea el numero.
c=round(a+b)
#resultado.Esto devuelve str por que esta envuelto en el formateo.
print(f"{c:,}")

#ahora con dividendo.
a=float(input("¿cual es a?"))
b=float(input("¿cual es b?"))
c=round(a/b, 2) #el ultimo numero indica cuantos decimales quedan detras de la coma.
print(c)
#de otra manera: print(f"{c: .2f})
