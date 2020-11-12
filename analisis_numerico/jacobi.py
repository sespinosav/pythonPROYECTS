from math import sqrt
print()
A = eval(input("Ingrese A: "))
b = eval(input("Ingrese b: "))
x0 = eval(input("Ingrese x0: "))
Tol = eval(input("Ingrese Tol: "))
Nmax = eval(input("Ingrese Nmax: "))

x1 = [0 for i in range(len(A))]
count = 0
disp = Tol + 1

def calcularNuevoJacobi(x0):
    for i in range(len(A)):
        sum1 = 0
        for j in range(len(A)):
            if j != i:
                sum1 += A[i][j]*x0[j]
        x1[i] = (b[i] - sum1)/A[i][i]
    return x1

def norma(x1,x0):
    result = 0
    for i, j in zip(x1,x0):
        result += (i-j)**2
    return sqrt(result)

while disp > Tol and count < Nmax:
    x1 = calcularNuevoJacobi(x0)
    disp = norma(x1,x0)
    x0 = [i for i in x1]
    count += 1
if disp < Tol:
    print(f"{x1} es aproximacion con una tolerancia = {Tol}")
else:
    print(f"Fracaso en {Nmax} iteraciones")

