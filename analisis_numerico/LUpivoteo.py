from gaussiana import formaMatrizAumentada, sustitucionProgresiva, sustitucionRegresiva, pivoteoParcial, intercambioMarcas, reordenar, printMatriz

A = eval(input("Ingrese A: "))
b = eval(input("Ingrese b: "))

L = [[0 for i in range(len(A))] for j in range(len(A))]
U = []
mults = []
def factorizacionLU(A, b, n):
    Ab = formaMatrizAumentada(A,b)  
    marcas = [i for i in range(n)]                   
    for k in range(n-1):
        L[k][k] = 1
        Ab, mayor = pivoteoParcial(Ab, n, k, True)
        if mayor != k:
            marcas = intercambioMarcas(marcas, mayor, k)
        mults_aux = {}
        for i in range(k+1, n):
            mults.append((i,k))
            mults_aux[(i,k)] = multiplicador = Ab[i][k] / Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] -= (multiplicador * Ab[k][j])
        for i, j in mults_aux:
            Ab[i][j] = mults_aux[(i,j)]
    L[len(L)-1][len(L)-1] = 1
    return Ab, marcas

Ab, marcas = factorizacionLU(A,b, len(A))
for i, j in mults:
    L[i][j] = Ab[i][j]

for i in Ab:
    U.append(i[:len(i)-1])

b = reordenar(b, marcas)
Lb = formaMatrizAumentada(L,b)
z = sustitucionProgresiva(Lb,len(L))
Uz = formaMatrizAumentada(U,z)
x = sustitucionRegresiva(Uz,len(U))
print()
print(x)
