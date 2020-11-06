def eliminacion(A, b, n):
    Ab = formaMatrizAumentada(A,b)
    for k in range(n-1):
        for i in range(k+1, n):
            multiplicador = Ab[i][k] / Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] -= (multiplicador * Ab[k][j])
    return Ab

def formaMatrizAumentada(A,b):
    Ab = A
    for a, b in zip(Ab, b):
        a.append(b)
    return Ab

def sustitucionRegresiva(Ab, n):
    x = [0 for i in range(n)]
    x[n-1] = Ab[n-1][n] / Ab[n-1][n-1]
    for i in range(n-1, -1, -1):
        sumatoria = 0
        for p in range(i+1, n):
            sumatoria += Ab[i][p] * x[p]
        x[i] = (Ab[i][n] -  sumatoria)/Ab[i][i]
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
            Ab = intercambioFilas(Ab, filaMayor, k)
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
        return Ab, marcas

def reordenar(x, marcas):
    x_aux = [i for i in x]
    orden = [i for i in range(len(x))]
    for i, j in zip(marcas,orden):
        x[i] = x_aux[j]
    return x
