import math
def calcular(f,x0,x1, E):
    error = 1
    i = 0
    x_e = 0
    signo = " ¡ "
    while error > E:
        i += 1
        xn = (x0+x1)/2
        error = abs((xn-x_e)/xn)
        x_e=xn
        print(i," | ",round(x0,6)," | ",round(x1,6)," | ",round(f(x0),6)," | ",round(f(x1),6)," | ",round(xn,6)," | ",round(f(xn),6)," | ",signo," | ", round(error,6))
        k = f(xn)*f(x0)
        if k > 0:
            x0 = xn
            signo = "+"
        elif k < 0:
            x1 = xn 
            signo = "-"
        elif f(xn)==0:
            return xn
        
        
    print("Se itero ",i," veces")
    return xn


error = 10**(-5) # Este es el error maximo
a = 0 # Esta es la cota inferior
b = 1 # ESta es la cota superior
y = lambda x: math.exp(x) - 2 + math.sin(2*x) # Esta es la función de la que se calcula su raíz
print("n  |  a    |  b    |  f(a)      |    f(b)     |  xn   |  f(xn)     |f(xn)*f(a)| E ")
sol = calcular(y,a,b,error)
print("La raiz xn = ", sol)