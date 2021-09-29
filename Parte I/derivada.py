import math
f = lambda x: 3*x**2+5*math.exp(x**2)

def derivada(f,x0): #calcula la derivada numérica
    h = 10**-9
    return round((f(x0+h)-f(x0))/h,6)

print(derivada(f,1))
