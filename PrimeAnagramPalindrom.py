lwr=int(input("Enter lower Range"))
upr=int(input("Enter upper Range"))

for i in range(lwr,upr+1):
	if i>1:
		for j in range(2,(i//2)+1):
			if i%j==0:
				break
		else:
			print(i,"is a prime number")
			num=i
			r=0
			rem=0
			while num!=0:
				r=num%10
				rem=rem*10+r
				num=num//10
			if rem==i:
				print("rem: :",rem,"is equal to ",i,"so Number is Palindrome")
			else:	
				print("rem: :",rem,"is Not equal to ",i,"so Number is Not Palindrome")
			d={}	
			
			