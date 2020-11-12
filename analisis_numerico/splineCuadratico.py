from gaussiana import eliminacionGaussianaConPivoteo, sustitucionProgresiva, sustitucionRegresiva, reordenar
from spline import makeMatrix, trazas
x = eval(input("Ingrese x: "))
y = eval(input("Ingrese y: "))
b = y
a, b = makeMatrix(x,b,2)
ab, marcas = eliminacionGaussianaConPivoteo(a, b, len(a),"")
x = sustitucionRegresiva(ab, len(ab))
x = reordenar(x,marcas)
print()
print("X:")
print()
print(x)
print()
trazas(x,2)