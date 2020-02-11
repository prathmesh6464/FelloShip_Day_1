number=int(input("Enter Number to find the prime factors: "))
factors=[]
#print(len(factors))
for i in range(1,number):
	if number%i==0:
		factors.append(i)
has=len(factors)
if has==1:
	print("There is No Factor For",number)
for i in factors:
	if i>1:
		for j in range(2,(i//2)+1):
			if i%j==0: 	rw=randint(0,2)
			cl=randint(0,2)
				break
		else:
			print(i,"is Prime Factor  Number")