HarmonicLimit=int(input("How Many Harmonic Number Do You Want To Print: "))
for i in range(1,HarmonicLimit+1):
	print("1 ",end="")
print()
for i in range(1,HarmonicLimit+1):
	if HarmonicLimit==i:
		
		res=0
		for j in range(1,HarmonicLimit+1):
			res=(1/i)
			res+=res
		print("- = ",res,end="")
	else:
		print("-+",end="")
print()
for i in range(1,HarmonicLimit+1):
	print(i,"",end="")
