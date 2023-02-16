import cmath

def area_trng(a,b,c):
    s=(a+b+c)/2
    a=(s*(s-a)*(s-b)*(s-c))**0.5
    return a

TNG=area_trng(5,6,7)
print(TNG)