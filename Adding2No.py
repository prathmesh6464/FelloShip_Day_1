t=int(input("Enter number for adding"))
def fun(t):
	print(t+(t-1))
	t-=1
	if t==1:
		return 1		
	fun(t)	
fun(t)