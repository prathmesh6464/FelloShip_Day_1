data=input("enter string for Merge Sorting : ").split()
def mergeSort(data):
	if len(data) >1:
		mid=len(data)//2
		left_list=data[:mid]
		right_list=data[mid:]
		mergeSort(left_list)
		mergeSort(right_list)
		j=0
		i=0
		k=0
		while i<len(left_list) and j<len(right_list):
			if left_list[i]<right_list[j]:
				data[k]=left_list[i]
				i+=1
				k+=1
			else:
				data[k]=right_list[j]
				j+=1
				k+=1
		while i<len(left_list):
			data[k]=left_list[i]
			k+=1
			i+=1
		while j<len(right_list):
			data[k]=right_list[j]
			j+=1
			k+=1

mergeSort(data)
print("After Merge Sort:",data)
			
		