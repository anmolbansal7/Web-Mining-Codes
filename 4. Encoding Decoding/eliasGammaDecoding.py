#Anmol Bansal 19BCE0630
#Elias Gamma Decoding

import math

def EliasGammaDecoding(n):
    n = list(n)
    K = 0
    while True:
        if not n[K] == '0':
            break
        K = K + 1
      
    n = n[K:2*K+1]
  
    a = 0
    n.reverse()
    
    for i in range(len(n)):
        if n[i] == '1':
            a = a+math.pow(2, i)
    return int(a)
  
n = input("Enter the Elias Gamma Encoded Value: ")
print(EliasGammaDecoding(n))