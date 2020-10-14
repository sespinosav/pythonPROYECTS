"""
read tolerancia, xa, niter
fx = f(xa)
contador = 0
error = tolerancia + 1
while fx != 0 and error > tolerancia and contador < niter do
    xn = g(xa)
    fx = f(xn)
    error = abs(xn - xa)
    xa = xn
    contador = contador + 1
end while
if fx = 0 then
    xa es raiz
else if error < tolerancia then
    xa es aproximacion con una tolerancia = tolerancia
else
    el metodo fracaso en niter iteracciones
end if
"""

from function import function as fun
import math

f = input("Ingrese la funcion f(x) (y = mx + b): ")
g = input("Ingrese la funcion g(x) (x = mx + b): ")
tole = float(input("Ingrese la tolerancia: "))
xa = float(input("Ingrese xa: "))
niter = float(input("Ingrese el numero maximo de iteracciones: "))

f = fun(f)
g = fun(g)
fx = f.evaluate(xa)
count = 0

err = tole + 1

while (fx != 0) and (err > tolerance) and (count < niter):
    xn = g.evaluate(xa)
    fx = f.evaluate(xn)
    err = math.fabs(xn - xa)
    xa = xn
    count += 1
if fx == 0:
    print("xa es raiz",xa)
elif err < tole:
    print("xa es aproximacion con una tolerancia:",xa)
else:
    print("El metodo fracaso en niter iteracciones",niter)
