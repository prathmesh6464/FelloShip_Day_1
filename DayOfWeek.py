from sys import argv
class DayOfWeek:
	@classmethod
	def dayOfWeek(cls,d,m,y):
		cls.d=int(d)
		cls.m=int(m)
		cls.y=int(y)
		cls.y=cls.y-(14-cls.m)//12
		print(cls.y)
		cls.x=cls.y+cls.y//4-cls.y//100+cls.y//400
		cls.m=cls.m+12*((14-cls.m)//12)-2
		print(cls.m)
		cls.d=(cls.d+cls.x+(31*cls.m)//12)%7
		print(cls.d)
		
DayOfWeek.dayOfWeek(argv[1],argv[2],argv[3])	