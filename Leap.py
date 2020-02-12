year=(input("Enter year: "))
if len(year)==4:
	year=int(year)
	if(year%4==0 and year%100!=0) or year%400==0:
		print(year,"is Leap Year")
	else:
				print(year,"is Not Leap Year")
else:
	print("Enter 4 digit Year Please")