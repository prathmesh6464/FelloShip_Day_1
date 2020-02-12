lwr=int(input("Enter lower range for prime number:"))
upr=int(input("Enter upper range for prime number:"))
for i in range(lwr,upr+1):
	if i>1:
		for j in range(2,(i//2)+1):
			if i%j==0:
				break
		else:
			print(i,"is Prime Number")