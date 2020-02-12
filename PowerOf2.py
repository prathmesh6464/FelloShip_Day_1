from sys import argv
cmdargv=int(argv[1])
L=[]
if 0<=cmdargv<31:
	for i in range(1,cmdargv+1):
		print(2**i)
		L.append(2**i)
for i in L:
	if (i%4==0 and i%100!=0 or i%400==0):
		print(i,"is leap year")	
	else:
		print(i,"is Not leap year")