from gaussiana import formaMatrizAumentada, sustitucionRegresiva, sustitucionProgresiva
from directa import factorizacionDirecta
A = eval(input("Ingrese A: "))
b = eval(input("Ingrese b: "))

L, U = factorizacionDirecta(A, "ch")
Lb = formaMatrizAumentada(L,b)
z = sustitucionProgresiva(Lb,len(L))
Uz = formaMatrizAumentada(U,z)
x = sustitucionRegresiva(Uz,len(U))
print()
print(x)
