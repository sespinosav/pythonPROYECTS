xs = eval(input("Ingrese los x: "))
ys = eval(input("Ingrese los y: "))

p = []
b = []

result = str(ys[0])
b.append(ys[0]) 
p.append(eval("lambda x: "+result))
b.append((ys[1]-b[0])/(xs[1]-xs[0]))
result += f"+{b[1]}*(x-{xs[0]})"
p.append(eval("lambda x: "+result))
print("lambda x: "+result)

for n in range(2,len(ys)):
    print(n)
    fun = p[n-1]
    den = 1
    coef = ""
    for i in xs[:n]:
        den *= (xs[n]-i)
        coef += f"(x-{i})*"
    coef = coef[:len(coef)-1]
    b.append((ys[n] - fun(xs[n]))/den)
    result += f"+{b[n]}*{coef}"
    p.append(eval("lambda x: "+result))
print(result)