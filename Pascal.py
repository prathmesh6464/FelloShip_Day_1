from numpy import *
n=int(input("Enter Number : "))
arr=ndarray(shape=(n,n),dtype=int)
for i in range(n):                   00
	for j in range(i+1):
		if j==0:
			#print(1,end=" ")
			arr[i][j]=1
		elif j==i:
			#print(1,end=" ")
			arr[i][j]=1
		else:
			arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
			
		print(arr[i][j],end=" ")
	print()
