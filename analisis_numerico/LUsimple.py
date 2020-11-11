from gaussiana import formaMatrizAumentada, sustitucionProgresiva, sustitucionRegresiva

A = eval(input("Ingrese A: "))
b = eval(input("Ingrese b: "))

L = [[0 for i in range(len(A))] for j in range(len(A))]
U = []
def factorizacionLU(A, b, n):
    Ab = formaMatrizAumentada(A,b)                      
    for k in range(n-1):
        L[k][k] = 1
        for i in range(k+1, n):
            L[i][k] = multiplicador = Ab[i][k] / Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] -= (multiplicador * Ab[k][j])
    L[len(L)-1][len(L)-1] = 1
    return Ab
    
Ab = factorizacionLU(A,b, len(A))
for i in Ab:
    U.append(i[:len(i)-1])

Lb = formaMatrizAumentada(L,b)
z = sustitucionProgresiva(Lb,len(L))
Uz = formaMatrizAumentada(U,z)
x = sustitucionRegresiva(Uz,len(U))
print()
print(x)
