from sys import argv
print(type(argv))
from math import sqrt,pow
x=int(argv[1])
y=int(argv[2])
calculate_distance = sqrt(pow(x,x)+pow(y,y))
print(calculate_distance)