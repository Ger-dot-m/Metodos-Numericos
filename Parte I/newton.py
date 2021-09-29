import math
def calcular(f, g, x0, E, complejo):
    error = 1
    xk = x0
    i = 0
    while error > E:
        xn = xk - f(xk)/g(xk)
        if complejo:
            xk = round(xk.real, 6) + round(xk.imag, 6) * 1j
            fOut = round(f(xk).real, 6) + round(f(xk).imag, 6) * 1j
            gOut = round(g(xk).real, 6) + round(g(xk).imag, 6) * 1j
        else:
            xk = round(xk,6)
            fOut = round(f(xk), 6)
            gOut = round(g(xk), 6)
        print(i," | ",xk,"\t| ", fOut,"\t| ",gOut,"\t| ",error)
        error = round(abs((xn-xk)/xn),6)
        i+=1
        xk = xn

    xn = xk - f(xk)/g(xk)
    if complejo:
        xk = round(xk.real, 6) + round(xk.imag, 6) * 1j
        fOut = round(f(xk).real, 6) + round(f(xk).imag, 6) * 1j
        gOut = round(g(xk).real, 6) + round(g(xk).imag, 6) * 1j
    else:
        xk = round(xk,6)
        fOut = round(f(xk), 6)
        gOut = round(g(xk), 6)
    print(i," | ",xk,"\t| ", fOut,"\t| ",gOut,"\t| ",error)
    error = round(abs((xn-xk)/xn),6)
    i+=1
    xk = xn
    return xn
        

x0 = -3.5
f = lambda x: x**3 - x**2 - 15*x + 1# function
g = lambda x: 3*x**2 - 2*x - 15 # derivada
error = 10**-5

print("n  |  xn+1\t\t| f(xn)\t\t| f'(xn)\t\t| E")
calcular(f,g,x0, error, 0)
