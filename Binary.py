num=int(input("Enter Number To Perform Binary Operations"))
def Binary(num):
	rem=""
	if num>128:
		pass
	while num>0:
		rem+=str(num%2)
		num=num//2
	
	s=rem.ljust(8,"0")
	rem=s[::-1]
	print(rem)
	first=rem[:4]
	second=rem[4:]
	res=(second+first)
	print(res)
	n=len(res)
	resVal=0
	for i in range(n):
		if res[(n-1)-i]=="1":
			resVal=resVal+2**i
	print(resVal)
Binary(num)