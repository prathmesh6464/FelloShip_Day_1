class VendingMachine:
	#def __init__(self):
	notes=[1,2,5,10,50,100,500,1000]
	#i=len(notes)
	@classmethod
	def enterAmount(cls,amt,i):
		if amt <=0:
			print("You Can Not Wthdraw amout you Entered Amout is less than or equals to zero (0) ")
		else:
			if amt in cls.notes:
				print(amt)
			else:
				if amt < cls.notes[i]:
					i-=1
					cls.enterAmount(amt,i)
				else:
					print(cls.notes[i])
					a=amt-cls.notes[i]
					cls.enterAmount(a,i)
				
				
	
v=VendingMachine
Amt=int(input("Widthdraw Money (money should be less than 100000): ")) 
i=7
v.enterAmount(Amt,i )
