from gaussiana import *
import numpy as np

xs = eval(input("Ingrese los x: "))
ys = eval(input("Ingrese los y: "))

A = []
b = ys

for i in xs:
    data = [(i)**k for k in range(len(xs))]
    data = data[::-1]
    A.append(data)

A = np.array(A)
A = np.linalg.inv(A)
b = np.array(b)
x = np.dot(A,b)
print(x)