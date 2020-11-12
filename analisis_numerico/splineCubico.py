from gaussiana import eliminacionGaussianaConPivoteo, sustitucionProgresiva, sustitucionRegresiva, reordenar
from spline import makeMatrix, trazas
x = eval(input("Ingrese x: "))
y = eval(input("Ingrese y: "))
b = y
a, b = makeMatrix(x,b,3)
ab, marcas = eliminacionGaussianaConPivoteo(a, b, len(a),"")
x = sustitucionRegresiva(ab, len(ab))
x = reordenar(x,marcas)

print()
print("Trazadores cubicos")
print()
print("Coeficientes:")
print()
result = ""
index = 0
for i in x:
    if index < 4:
        index += 1
        result += f"{i:.5f} "
    else:
        print(result)
        result = f"{i:.5f} "
        index = 1
print(result)
print()
trazas(x, 3)