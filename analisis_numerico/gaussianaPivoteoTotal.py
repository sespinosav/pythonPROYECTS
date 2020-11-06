from gaussiana import eliminacionGaussianaConPivoteo, sustitucionRegresiva, reordenar

A = eval(input("Ingrese la matriz A: "))
b = eval(input("Ingrese el arreglo b: "))

Ab, marcas = eliminacionGaussianaConPivoteo(A, b, len(A),"")
x = sustitucionRegresiva(Ab, len(A))
x = reordenar(x, marcas)
print(x)
