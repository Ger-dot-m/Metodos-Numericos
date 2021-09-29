import math
def calcular(f, x0, x1, E):
    error = 1
    i = 1
    while error > E:
        try: xn = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        except: break
        x0 = round(x0,6)
        x1 = round(x1,6)
        xn = round(xn, 6)
        if i==1: error = "xxx"
        else: 
            try:
                error = round(abs((xn-x1)/xn),6)
            except:
                break
        print(i," | ",x0,"\t| ", x1,"\t| ", round(f(x0),6),"\t| ", round(f(x1),6),"\t\t| ",xn,"\t| ", round(f(xn),6),"\t\t| ",error)
        error = 1
        i+=1
        x0 = x1
        x1 = xn
    return xn
        

x0 = 2
x1 = 3
f = lambda x: x**3 - (2*x**2)*math.sin(x) # function
error = 10**-5

print("n  |  xn-1\t\t| xn \t\t| f(xn-1)\t\t| f(xn)\t\t| xn+1\t\t| f(xn+1)\t\t| E")
calcular(f,x0,x1, error)
