"""
read tol, x0, niter
fx = f(x0)
dfx = f'(x0)
contador = 0
error = 0
error = tol + 1

while err > tol and fx != 0 and dfx != 0 and contador < niter do
    x1 = x0 - fx/dfx
    fx = f'(x1)
    dfx = f'(x1)
    error = abs(x1 - x0)
    x0 = x1
    contador = contador + 1
end while
if fx = 0 then
    x0 es raiz
else if error < tol then
    x1 es es aproximacion a una raiz con una tolerancia = tol
else if dfx = 0 then
    x1 es una posible raiz multiple
else
    fracaso en niter iteraciones
end if
"""

from function import function as fun
import math

f = input("Ingrese la funcion: ")
dfx = input("Ingrese la derivada de la funcion: ")
tol = float(input("Ingrese la tolerancia: "))
x0 = float(input("Ingrese x0: "))
niter = float(input("Ingrese el maximo de iteraciones: "))

f = fun(f)
df = fun(dfx)

fx = f.evaluate(x0)
dfx = df.evaluate(x0)

count = 0
err = 0
err = tol + 1

while (err > tol) and (fx != 0) and (dfx != 0) and (count < niter):
    x1 = x0 - fx/dfx
    fx = f.evaluate(x1)
    dfx = df.evaluate(x1)
    err = math.fabs(x1 - x0)
    x0 = x1
    count += 1
if fx = 0:
    print("x0 es raiz",x0)
elif err < tol:
    print("x1 es aproximacion a una raiz con una tolerancia:",tol)
elif dfx = 0:
    print("x1 es una posible raiz multiple",x1)
else:
    print("Fracaso en " + niter + " iteraciones")
