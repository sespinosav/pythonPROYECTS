from gaussiana import *

A = eval(input("Ingrese A: "))
b = eval(input("Ingrese b: "))

L = [[0 for i in range(len(A))] for j in range(len(A))]
U = []
def eliminacionLU(A, b, n):
    Ab = formaMatrizAumentada(A,b)                      
    for k in range(n-1):
        L[k][k] = 1
        for i in range(k+1, n):
            multiplicador = Ab[i][k] / Ab[k][k]
            L[i][k] = multiplicador
            for j in range(k, n+1):
                Ab[i][j] -= (multiplicador * Ab[k][j])
    return Ab
Ab = eliminacionLU(A,b, len(A))
for i in Ab:
    U.append(i[:len(i)-1])

Lb = formaMatrizAumentada(L,b)
z = sustitucionProgresiva(Lb,len(L))
Uz = formaMatrizAumentada(U,z)
x = sustitucionRegresiva(Uz,len(U))
print(x)
