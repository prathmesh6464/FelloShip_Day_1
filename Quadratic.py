from math import sqrt
a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))
delta = b*b - 4*a*c
print(delta)       
Root1ofx=(-b+sqrt(delta))/(2*a)
Root2ofx=(-b-sqrt(delta))/(2*a)
print("Root 1 of x : ",Root1ofx)
print("Root 2 of x : ",Root2ofx)

