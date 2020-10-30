
import math
f = eval(input("Ingrese la funcion: "))
x0 = float(input("Ingrese x0: "))
delta = float(input("Ingrese delta: "))
niter = float(input("Ingrese el numero maximo de iteracciones: "))

fx0 = f(x0)

if fx0 == float(0):
    print("x0 es raiz:",x0)
else:
    x1 = x0 + delta
    count = 1
    fx1 = f(x1)

    while ((fx0 * fx1) > 0.0) and (count < niter):
        x0 = x1
        fx0 = fx1
        x1 = x0 + delta
        fx1 = f(x1)
        count += 1
    
    if fx1 == 0:
        print("x1 es raiz:",x1)
    elif (fx0 * fx1) < 0:
        print("Hay un raiz entre x0 y x1:",x0,x1)
    else:
        print("Fracaso en " + str(niter) + " iteracciones")
