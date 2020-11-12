from gaussiana import formaMatrizAumentada, sustitucionProgresiva, sustitucionRegresiva

A = eval(input("Ingrese A: "))
b = eval(input("Ingrese b: "))
etapa = 0

L = [[0.0 for i in range(len(A))] for j in range(len(A))]
A = [[float(i) for i in j] for j in A]
U = []
def factorizacionLU(A, b, n, etapa):
    Ab = formaMatrizAumentada(A,b)                      
    for k in range(n-1):
        L[k][k] = 1.0
        for i in range(k+1, n):
            L[i][k] = multiplicador = Ab[i][k] / Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] -= (multiplicador * Ab[k][j])
        etapa += 1
        print()
        print(f"Etapa {etapa}")
        print()
        print("L:")
        for i in L:
            result = ""
            for j in i:
                text = str(j)
                text += "000000"
                result += text[:7]+" "
            print(result)
        print()
    L[len(L)-1][len(L)-1] = 1.0

    return Ab
    
print("LU con gaussiana simple:")
print()
print("Resultados")
print()
print(f"Etapa {etapa}")
print()
for i in A:
    result = ""
    for j in i:
        text = str(j)
        text += "0000"
        result += text[:7]+" "
    print(result)
print()
Ab = factorizacionLU(A,b, len(A),etapa)
for i in Ab:
    U.append(i[:len(i)-1])

print("U:")
for i in [i[:len(i)-1] for i in Ab]:
    result = ""
    for j in i:
        text = str(j)
        text += "0000"
        result += text[:7]+" "
    print(result)
print()

Lb = formaMatrizAumentada(L,b)
z = sustitucionProgresiva(Lb,len(L))
Uz = formaMatrizAumentada(U,z)
x = sustitucionRegresiva(Uz,len(U))
print()
print(x)
