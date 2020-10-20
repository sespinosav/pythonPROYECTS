"""
#Dado Ax = b
Macro algoritmo de la eliminacion gaussiana simple

read A,b

U, B = Eliminacion(A,b) #Volver triangular superior Ux = B

x = Despeje(U,B)
print x

#Eliminacion gausssiana sin intercambio de filas

function ELIMINACION(A, b, n)
    Ab = FormaMatrizAumentada(A,b)
    for k = 1 to n-1 do
        for i = k + 1 to n do
            multiplicador = Abik / Abkk
            for j = k to n + 1 do
                Abij = Abij - multiplicador * Abkj
            end for
        end for
    end for
    return Ab


#Sustitucion regresiva 

function SUSTITUCIONREGRESIVA(Ab, n)
    xn = Abnn+1 / Abnn
    for i = n - 1 to 1 step -1 do
        sumatoria = 0
        for p = i + 1 to n do
            sumatoria = sumatoria + Abip * xp
        end for
    end for
    xi = (Abin+1 - sumatoria)/Abii
    return x

#Estructura de eliminacion gaussiana con pivoteo

function ELIMINACIONGAUSSIANACONPIVOTEO(A, B, n)
    Ab = FormaMatrizAumentada(A,b)
    for k = 0 to n - 1 do
        Ab = Pivoteo(Ab, n, k)
        for i = k + 1 to n do
            multiplicador = Abik / Abkk
            for j = k to n + 1 do
                Abij = Abij - multiplicador * Abkj
            end for
        end for
    end for
    return Ab
end function

#Pivoteo parcial

function PIVOTEOPARCIAL(Ab, n, k)
    mayor = abs(Abkk)
    filaMayor = k
    for s = k + 1 to n do
        if abs(Absk) > Mayor then
            mayor = abs(Absk)
            filaMayor = s
        end if
    end for
    if mayor = 0
        return 'El sistema no tiene solucion unica"
    else
        if filaMayor != k then
            Ab = IntercambioFilas(Ab, filaMayor, k)
        end if
        return Ab
    end if
end function

#Pivoteo total

function PIVOTEOTOTAL(Ab, n, k)
    mayor = 0
    filaMayor = k
    columnaMayor = k
    for r = k to n do
        for s = k to n do
            if abs(Abrs) > mayor then
                mayor = abs(Abrs)
                filaMayor = r
                columnaMayor = s
            end if
        end for
    end for
    if mayor = 0 then
        return El sistema no tiene solucion unica
    else
        if filaMayor != k then
            Ab = intercambieFilas(Ab, filaMayor, k)
        end if
        if columnaMayor != k then
            Ab = intercambieColumnas(Ab, columnaMayor)
            marcas = intercambieMarcas(marcas,columnasMayor,k)
        end if
        return Ab, marcas
    end if
end function
"""
def eliminacion(A, b, n):
    Ab = formaMatrizAumentada(A,b)
    for k in range(n-1):
        for i in range(k+1, n):
            multiplicador = Ab[i][k] / Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] -= multiplicador * Ab[k][j]
    return Ab

def formaMatrizAumentada(A,b):
    Ab = A
    for a, b in zip(Ab, b):
        a.append(b)
    return Ab

def sustiticionRegresiva(Ab, n):
    x = [0 for i in range(n)]
    x[n-1] = Ab[n-1][n] / Ab[n-1][n-1]
    for i in range(n-2, -1, -1):
        sumatoria = 0
        for p in range(i+1, n):
            sumatoria += Ab[i][p] * x[p]
        x[i] = (Ab[i][n])/Ab[i][i]
    return x

def intercambioFilas(Ab, filaMayor, k):
    filaAux = Ab[k]
    Ab[k] = Ab[filaMayor]
    Ab[filaMayor] = filaAux
    return Ab

def intercambioColumnas(Ab, columnaMayor, k):
    columAux = [Ab[i][k] for i in range(len(Ab))]
    for i in range(len(Ab)):
        Ab[i][k] = Ab[i][columnaMayor]
    for i in range(len(Ab)):
        Ab[i][columnaMayor] = columAux[i]
    return Ab

def pivoteoParcial(Ab, n, k):
    mayor = abs(Ab[k][k])
    filaMayor = k
    for s in range(k+1, n):
        if abs(Ab[s][k]) > mayor:
            filaMayor = s
        if mayor == 0:
            print("El sistema no tiene solucion unica")
            return 0
        else:
            if filaMayor != k:
                Ab = intercambioFilas(Ab, filaMayor, k)
            return Ab

def intercambioMarcas(marcas, columnaMayor, k):
    marcaAux = marcas[k]
    marcas[k] = marcas[columnaMayor]
    marcas[columnaMayor] = marcaAux

    return marcas

def pivoteoTotal(Ab, n, k, marcas):
    mayor = 0
    filaMayor = k
    columnaMayor = k
    for r in range(k, n):
        for s in range(k, n):
            if abs(Ab[r][s]) > mayor:
                mayor = abs(Ab[r][s])
                filaMayor = r
                columnaMayor = s
    if mayor == 0:
        print("El sistema no tiene solucion unica")
        return 0
    else:
        if filaMayor != k:
            Ab = intercambieFilas(Ab, filaMayor, k)
        if columnaMayor != k:
            Ab = intercambioColumnas(Ab, columnaMayor, k)
            marcas = intercambioMarcas(marcas, columnaMayor, k)
        return Ab, marcas

def eliminacionGaussianaConPivoteo(A, b, n, pivoteo="parcial"):
    Ab = formaMatrizAumentada(A, b)
    if pivoteo == "parcial":
        pivoteo = pivoteoParcial
        for k in range(n-1):
            Ab = pivoteo(Ab, n, k)
            for i in range(k + 1, n):
                multiplicador = Ab[i][k] / Ab[k][k]
                for j in range(k, n+1):
                    Ab[i][j] -= multiplicador * Ab[k][j]
        return Ab
    else:
        pivoteo = pivoteoTotal
        marcas = [i for i in range(n)]
        for k in range(n-1):
            Ab, marcas = pivoteo(Ab, n, k, marcas)
            for i in range(k + 1, n):
                multiplicador = Ab[i][k] / Ab[k][k]
                for j in range(k, n+1):
                    Ab[i][j] -= multiplicador * Ab[k][j]
        print("El orden de las variables es:", marcas)
        return Ab
