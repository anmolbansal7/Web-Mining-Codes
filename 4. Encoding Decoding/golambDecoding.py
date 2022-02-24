# Anmol Bansal 19BCE0630
# Golomb Decoding

import math

def UnarytoQ(c):
    return len(c)-1

def SplitCode(c):
    t = c.find('1')
    return c[:t+1], c[t+1:]

def BinarytoDec(n):
    return int(n,2)

def GolombDecode(c, b):
    m, n = SplitCode(c)
    q = UnarytoQ(m)
    i = math.floor(math.log(b, 2))
    d = 2**(i+1) - b
    r1 = n[:i]
    r = BinarytoDec(r1)
    if(r>=d):
        r1 = r1 + n[i:i+1]
        r = BinarytoDec(r1) - d
    
    x = q*b+r
    return x


x=str(input("Enter the Golomb Encoded Value: "))
b=int(input("Enter value of b: "))
print("\n")

y = GolombDecode(x, b)

print("Original Value: ", y)  