f=open(r"C:\Users\User\Desktop\new.txt","r")
h=f.readline().split()
print(h)
k=0
for i in range(len(h)-1):
	for j in range(len(h)-1-i):
		k+=1
		if h[j]>h[j+1]:
			h[j],h[j+1]=h[j+1],h[j]
print(h)
print("k values : ",k)
search=input("Enter The Word For Search : ")
u=len(h)-1
l=0

mid=u+l//2
try:
	s=0
	while h[mid]!=search:
		
		if h[mid]<search:
			l=mid+1
			mid=u+l//2
			s+=1
		else:
			u=mid-1
			mid=u+l//2 
			s+=1
except BaseException:
	print("Searched Value Not Found")
try:
	if h[mid]==search:
		print(h[mid], "value is at index Number : ",mid)
except BaseException:
	pass
print(s)
f.close()