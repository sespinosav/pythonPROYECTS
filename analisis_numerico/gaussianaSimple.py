from gaussiana import *

A = eval(input("Ingrese la matriz A: "))
b = eval(input("Ingrese el arreglo b: "))

Ab = eliminacion(A, b, len(A))
x = sustiticionRegresiva(Ab, len(A))

print(x)
