from random import randint
BalanceMoney=float(input("Enter Balance Money of Gambler "))
Stack=float(input("Enter Stak"))
Goal=float(input("Enter Goal"))
#NumberOfTimes=int(input("Enter Number Of Times"))
class gambler:
	def __init__(self,BalanceMoney=0,Goal=0,Stack=0,win=0,lose=0):
		self.BalanceMoney=BalanceMoney
		self.Goal=Goal
		self.Stack=Stack
		self.win=win
		self.lose=lose
		self.PlayedNum=0
	def feedBalance(self,BalanceMoney):
		self.BalanceMoney=BalanceMoney
	def feedStack(self,stack):
		self.Stack=stack
	def	feedGoal(self,Goal):
		self.Goal=Goal
	def start(self):
		if BalanceMoney<=0:
			print("Sorry You Can't Play your Account Balance is zer0")
		else:
			while self.Goal!=self.win and self.BalanceMoney!=0:
				val=randint(0,1)
				self.PlayedNum+=1
				if val==0:
					self.lose+=1
					print("You lost")					
					self.BalanceMoney-=self.Stack
				else: 
					self.win+=1
					print("You win")
					#self.Goal+=1
					self.BalanceMoney+=self.Stack
			
				"""if self.win==self.Goal:
					print("You achieved your goal")
				
				else:
					print("Goal is Not achieved you can play again ")"""
					
	def	getPercentOfWin(self):
		if (self.PlayedNum==0):
			print("you should play atlest one game")
		else:
			print("Percent Of win : ",self.win*100/self.PlayedNum)
	def getPercentOflose(self):
		if (self.PlayedNum==0):
			print("you should play atlest one game")
		else:
			print("Percent Of Lose : ",self.lose*100/self.PlayedNum)
	def getBalancedMoney(self):
		print("Balanced Money : ",self,BalanceMoney)
			
pratham=gambler(BalanceMoney,Goal,Stack)
pratham.feedGoal(Goal)
pratham.feedStack(Stack)
pratham.feedBalance(BalanceMoney)
pratham.start()
pratham.getBalancedMoney()
pratham.getPercentOfWin()
pratham.getPercentOflose()
pratham.getBalancedMoney()