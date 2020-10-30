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
import math

f = eval(input("Ingrese la funcion f: "))
g = eval(input("Ingrese la funcion g: "))
tole = float(input("Ingrese la tolerancia: "))
xa = float(input("Ingrese xa: "))
niter = float(input("Ingrese el numero maximo de iteracciones: "))

fx = f(xa)
count = 0
xn = xa

err = tole + 1

while (fx != 0) and (err > tole) and (count < niter):
    print(count,xn,f(xn),err)
    xn = g(xa)
    fx = f(xn)
    err = abs((xn - xa)/xn)
    xa = xn
    count += 1

if fx == 0:
    print("xa es raiz",xa)
elif err < tole:
    print("xa: ",xa ,"es aproximacion con una tolerancia:",tole)
else:
    print("El metodo fracaso en niter iteracciones",niter)
