import math
from sys import argv
t=eval(argv[1])
v=eval(argv[2])
if t<50 and (v<=120 and v>=3):
	print("Wind Chill : ",35.74+0.6215*t+(0.4275*t-3575)*math.pow(v,0.16))
else:
	print("Formula is Not Valid")