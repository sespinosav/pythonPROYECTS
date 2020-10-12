"""
read tol, x0, x1, niter
fx0 = f(x0)
if fx0 = 0 then
    x0 es raiz
else
    fx1 = f(x1)
    cont = 0
    error = tol + 1
    den = fx1 - fx0
    while error > tol and fx1 != 0 and den != 0 and cont < niter do
        x2 = x1 - fx1 * (x1 - x0)/den
        error = abs(x2 - x1)
        x0 = x1
        fx0 = fx1
        x1 = x2
        fx1 = f(x1)
        den = fx1 - fx0
        cont = cont + 1
    end while
    if fx1 = 0 then
        x1 es raiz
    else if error < tol then
        x1 es aproximacion a una raiz con una tolerancia = tol
    else if den = 0 then
        hay una posible raiz multiple
    else
        fracaso en niter iteraciones
    end if
end if
"""
