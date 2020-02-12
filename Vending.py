class Vending:
	notes=[1,2,5,10,50,100,500,1000]
	def __init__(self):
		self.amt=0

	def withDraw(self,amt,l):

		if amt<=0:
			print("amout should be greater than zero")
		else:
			if amt in Vending.notes:
				print(amt,"withdraw")
			else:
				
				if amt<Vending.notes[l]:
					l=l-1
					self.withDraw(amt,l)
				else:
					print(Vending.notes[l])
					a=amt-Vending.notes[l]
					self.withDraw(a,l) 
			
no=int(input("Enter Amount : "))
v=Vending()
v.withDraw(no,7)
					
					
					
				
		