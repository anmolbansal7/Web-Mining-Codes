# Anmol Bansal 19BCE0630
# Golomb Encoding

import math

def Binary(n):
    return "{0:b}".format(int(n))

def Unary(x, b):
    q = x//b
    r = x - q*b
    res = '0'*q+'1'
    return r, res

def GolombEncoding(x, b):
    r, unary = Unary(x, b)
    
    i = math.floor(math.log(b, 2))
    
    d = 2**(i+1) - b
    temp = None
    if(r<d):
        temp = Binary(r)
        if(len(temp) < i):
            temp = '0'*(i-len(temp))+temp
        else:
            temp = temp[-i:]
    else:
        t = r + d
        temp = Binary(t)
        if(len(temp) < (i+1)):
            temp = '0'*((i+1)-len(temp))+temp
        else:
            temp = temp[-(i+1):]
    
    return unary+temp

x = int(input("Enter the value to be encoded: "))
b = int(input("Enter value of b: "))
print("\n")

y = GolombEncoding(x, b)

print("Golomb Code: ", y)
