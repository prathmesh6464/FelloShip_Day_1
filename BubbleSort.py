input=eval(input("Enter a integer List Values : "))
def bubbleSort():
	for i in range(len(input)-1):
		for j in range(len(input)-1-i):
			if input[j]>input[j+1]:
				input[j],input[j+1]=input[j+1],input[j]
	print(input)
bubbleSort()