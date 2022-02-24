#Anmol Bansal 19BCE0630
#Elias Delta Decoding

import math

def EliasDeltaDecoding(n):
	n = list(n)
	L=0
	while True:
		if not n[L] == '0':
			break
		L= L + 1
	
	n=n[2*L+1:]
	
	n.insert(0,'1')
	n.reverse()
	a=0
	
	for i in range(len(n)):
		if n[i]=='1':
			a=a+math.pow(2,i)
	return int(a)

n = input("Enter the Elias Delta Encoded Value: ")
print(EliasDeltaDecoding(n))
