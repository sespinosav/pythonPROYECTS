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
