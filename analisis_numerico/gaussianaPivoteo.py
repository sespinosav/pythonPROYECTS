from gaussiana import *

A = eval(input("Ingrese la matriz A: "))
b = eval(input("Ingrese el arreglo b: "))

Ab = eliminacionGaussianaConPivoteo(A, b, len(A))
print(Ab)
x = sustitucionRegresiva(Ab, len(A))

print(x)
