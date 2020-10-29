xs = eval(input("Ingrese los x: "))
ys = eval(input("Ingrese los y: "))


expresion = ""
result = 1
polim = "*"
for i in xs:
    for k in xs:
        if xs.index(i) != xs.index(k): 
            polim += ("(x - "+str(k)+")*")
            result *= i - k  
    polim = polim[0:len(polim)-1]
    result = 1/result
    result = ys[xs.index(i)]*result
    expresion += "("+str(result)+polim+")"+"+"
    polim = "*"
    result = 1
expresion = expresion[0:len(expresion)-1]
print(expresion)