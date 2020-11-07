import numpy as np
from gaussiana import eliminacionGaussianaConPivoteo, sustitucionRegresiva, reordenar

xs = eval(input("Ingrese los x: "))
ys = eval(input("Ingrese los y: "))

A = []
b = ys

for i in xs:
    data = [(i)**k for k in range(len(xs))]
    data = data[::-1]
    A.append(data)
    
Ab, marcas = eliminacionGaussianaConPivoteo(A, b, len(A),"")
x = sustitucionRegresiva(Ab, len(A))
x = reordenar(x, marcas)

result = ""
coef = len(x)
for i in x:
    coef -= 1
    if coef != 0:
        if i >= 0.0:
            result += "+"+str(i)+"*"+"x**"+str(coef)
        else:
            result += str(i)+"*"+"x**"+str(coef)
    else:
        if i >= 0.0:
            result += "+"+str(i)
        else:
            result += str(i)

print(result)    
