#Anmol Bansal 19BCE0630
#Elias Delta Encoding

from math import log
from math import floor

def BinaryRepresentationWithoutMSB(x):
	binary = "{0:b}".format(int(x))
	binaryWithoutMSB = binary[1:]
	return binaryWithoutMSB

def EliasGammaEncode(k):
	if (k == 0):
		return '0'
	N = 1 + floor(log(k, 2))
	Unary = (N-1)*'0'+'1'
	return Unary + BinaryRepresentationWithoutMSB(k)

def EliasDeltaEncode(x):
	Gamma = EliasGammaEncode(1 + floor(log(k, 2)))
	binaryWithoutMSB = BinaryRepresentationWithoutMSB(k)
	return Gamma + binaryWithoutMSB

k = int(input("Enter the value: "))
print(EliasDeltaEncode(k))
