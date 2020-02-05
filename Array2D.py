from numpy import *
M=int(input("how to many Rows Do you want to Enter: "))
N=int(input("how to many Columns Do you want to Enter: "))
#dataType=input("which type of data do you want in your Array: ")
print("Please Enter",M*N,"Numbers")
arr=ndarray(shape=(M,N),dtype=int)
#arr = [[0]*M]*N
for i in range(M):
	for j in range(N):
		arr[i][j]=int(input("Enter Data In Array: "))
print(arr)