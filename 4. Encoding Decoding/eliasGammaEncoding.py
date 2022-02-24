#Anmol Bansal 19BCE0630
#Elias Gamma Encoding

from math import log

log2 = lambda n: log(n, 2)
  
def Unary(n):
    return (n-1)*'0'+'1'
  
def Binary(n, l = 1):
    s = '{0:0%db}' % l
    return s.format(n)
      
def EliasGamma(n):
    if(n == 0): 
        return '0'
  
    a = 1 + int(log2(n))
    b = n - 2**(int(log2(n)))
  
    l = int(log2(n))
  
    return Unary(a) + Binary(b, l)

number = int(input("Enter the Number: "));
print(EliasGamma(number))