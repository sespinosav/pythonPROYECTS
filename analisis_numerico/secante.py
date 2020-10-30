import math
f = eval(input("Ingrese la funcion: "))
x0 = float(input("Ingrese x0: "))
x1 = float(input("Ingrese x1: "))
tol = float(input("Ingrese la tolerancia: "))
niter = float(input("Ingrese el maximo de iteraccion: "))

fx0 = f(x0)

if fx0 == 0:
    print("x0 es raiz: ",x0)
else:
    fx1 = f(x1)
    cont = 0
    error = tol + 1
    den = fx1 - fx0
    while error > tol and fx1 != 0 and den != 0 and cont < niter:
        x2 = x1 - fx1 * (x1 - x0)/den
        error = abs(x2 - x1)
        x0 = x1
        fx0 = fx1
        x1 = x2
        fx1 = f(x1)
        den = fx1 - fx0
        cont += 1
    if fx1 == 0:
        print("x1 es raiz ",x1)
    elif error < tol:
        print("x1: ", x1, "es aproximacion a una raiz con una tolerancia: ", tol)
    elif den == 0:
        print("Hay una posible raiz multiple")
    else:
        print("Fracasó en niter iteraciones: ", niter)
