f = eval(input("Ingrese la funcion: "))
df = eval(input("Ingrese la derivada de la funcion: "))
tol = float(input("Ingrese la tolerancia: "))
x0 = float(input("Ingrese x0: "))
niter = float(input("Ingrese el maximo de iteraciones: "))

fx = f(x0)
dfx = df(x0)

count = 0
err = 0
err = tol + 1

while (err > tol) and (fx != 0) and (dfx != 0) and (count < niter):
    x1 = x0 - fx/dfx
    fx = f(x1)
    dfx = df(x1)
    err = abs(x1 - x0)
    x0 = x1
    count += 1
    print("i: ",count,"x0: ",x0,"x1: ",x1,"e: ",err)
print()
if fx == 0:
    print("x0 es raiz",x0)
elif err < tol:
    print("x1 es aproximacion a una raiz con una tolerancia:",x1, tol)
elif dfx == 0:
    print("x1 es una posible raiz multiple",x1)
else:
    print("Fracaso en " + niter + " iteraciones")
