import math
R=float(input("Radiusini kiriting R="))
n=int(input("nechta burchak ekanini kiriting n="))
P=2*n*R*math.sin(math.pi/n)
print("perimetri", P)
S=(n*R**2*math.sin(2*math.pi/n))/2
print("yuzasi", S)