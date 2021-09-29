def division(coef_pre,r,s):
    i = 1
    k = 0
    coef = copia(coef_pre)
    for x in coef:
        if i > 1: k = coef[i-2]
        try: 
            coef[i] = round(coef[i] + coef[i-1]*r + k*s,6)
            i += 1
        except: break
    return coef

def solveCrammer(M1, M2):
    a = [ M1[-i-1] for i in range(len(M1))]
    b = [ M2[-i-1] for i in range(len(M2))]
    det = b[1]**2 - b[2]*b[0]
    dr = -a[1]*b[1]+a[0]*b[2]
    ds = -b[1]*a[0]+a[1]*b[0]
    return dr/det, ds/det

def copia(x):
    y=[]
    for elmnt in x:
        y.append(elmnt)
    return y

error = lambda x,y: abs(x/y)*100

def Bairstow(r,s, arreglo, E):
    Er = 100
    Es = 100
    while(Er > E and Es > E):
        B = division(arreglo,r,s)
        k = copia(B)
        del B[-1]
        C = division(B,r,s)
        delta = solveCrammer(k,C)
        r = round(r + delta[0],6)
        s = round(s + delta[1],6)
        Er = error(delta[0],r)
        Es = error(delta[1],s)
        print("r = ", r," s = ", s)
    



# Planteamiento del problema
r = -1
s = -1
array = [1,-2, 6, -2, 5] # array de coeficientes

Bairstow(r,s,array, 5)