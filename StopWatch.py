import time
class StopWatch:
	second=0
	Minute=0
	Hour=0
	def start(cls):
		print()
		print("If You Want To Stop StopWatch Then Enter ctrl+c")
		print()
		try:
			while 1:
				
				time.sleep(1)
				cls.second+=1
				if cls.second==60:
					cls.Minute+=1
					cls.second=0
				if cls.Minute==60:
					cls.Hour+=1
				print(cls.Hour,":",cls.Minute,":",cls.second)
		except KeyboardInterrupt as k:
			print("Stop Watch Timing : " ,cls.Hour,":",cls.Minute,":",cls.second)
		
s=StopWatch()
s.start()
	