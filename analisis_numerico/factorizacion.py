from gaussiana import *
def factorizacion(A,b,n):
    L,U = factorizacionLU(A,n)
    Lb = formaMatrizAumentada(L,b)
    z = sustitucionProgresiva(Lb,len(L))
    Uz = formaMatrizAumentada(U,z)
    x = sustitucionRegresiva(Uz,len(U))
    return x
