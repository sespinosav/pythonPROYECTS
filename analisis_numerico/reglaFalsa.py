import math

#xi,xs,tolerance,niter

f = eval(input("Ingrese la funcion: "))
xi = float(input("Ingrese xi: "))
xs = float(input("Ingrese xs: "))
tolerance = float(input("Ingrese la tolerancia: "))
niter = float(input("Ingrese el maximo de iteraccion: "))

fxi = f(xi)
fxs = f(xs)

if fxi == 0:
    print("xi es una raiz",xi)
elif fxs == 0:
    print("xs es una raiz",xs)
elif (fxi * fxs) < 0:
    xm = (xi) - ((fxi*(xs-xi)) / (fxs-fxi))
    fxm = f(xm)
    count = 1
    error = tolerance + 1

    while (error > tolerance) and (fxm != 0) and (count < niter):
        if (fxi * fxm) < 0:
            xs = xm
            fxs = fxm
        else:
            xi = xm
            fxi = fxm
        xaux = xm
        xm = (xi) - ((fxi*(xs-xi)) / (fxs-fxi))
        fxm = f(xm)
        error = abs(xm - xaux)
        count += 1
    if fxm == 0:
        print("xm es rai",xm)
    elif error < tolerance:
        print("xm "+str(xm)+" es aproximacion a una raiz con una tolerancia:",tolerance)
    else:
        print("Fracaso en " + str(niter) + " iteracciones")
else:
    print("El intervalo es inedacuado")







