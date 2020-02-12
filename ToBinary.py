num=int(input("Please Enter Integer Value to Convert into Binary number"))
def toBin(num):
	rem=''
	while num>0:
		rem=rem+str(num%2)
		num=num//2
	print(rem[::-1])
toBin(num)