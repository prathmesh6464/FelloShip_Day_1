string1=input("Enter First String").split()
string2=input("Enter First String").split()
def sorting(strings):
	for i in range(len(strings)):
		minindex=i
		j=i
		while j<len(strings):
			if strings[minindex]>strings[j]:
				minindex=j
			j+=1
		strings[i],strings[minindex]=strings[minindex],strings[i]
	print(strings)
	return strings
if sorting(string1)==sorting(string2):
	print("String is anagram ")
else:
	print("String is Not Anagram")