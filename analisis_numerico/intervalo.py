#Generate a interval whit a raiz

import math

f = eval(input("Ingrese la funcion: "))
x0 = eval(input("Ingrese x0: "))
delt = eval(input("Ingrese delta: "))

fx0 = f(x0)
x1 = x0 + delt
fx1 = f(x1)
val = False

for i in range(999999999999999):
    if fx0 == 0:
        print(f"{x0} es raiz")
        val = True
    if fx1 == 0:
        print(f"{x1} es raiz")
        val = True
    elif fx0 * fx1 < 0:
        print(f"[{x0},{x1}]")
        val = True
    if val:
        break
    x0 = x1
    x1 = x0 + delt
    fx0 = f(x0)
    fx1 = f(x1)
if val == False:
    print("Not found")
