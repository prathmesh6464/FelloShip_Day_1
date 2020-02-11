from random import randint
from numpy import ndarray
NumArray=int(input("Enter how many number do you want to Enter into array : "))
arr=ndarray(shape=(NumArray,),dtype=int)
for i in range(NumArray):
	tempNum=randint(-100,100)
	arr[i]=tempNum
print(arr)
i=0;j=1;k=2
while k<NumArray:
	if (arr[i]+arr[j]+arr[k])==0:
		print(arr[i],arr[j],arr[k],"this number sum is zero (0)")
		#break
	else:
		print(arr[i],arr[j],arr[k],"this number sum is Not zero (0)")
	i+=1;j+=1;k+=1