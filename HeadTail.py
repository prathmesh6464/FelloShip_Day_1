from random import random
Flip_Nos=int(input("How many times do you want to flip coin: "))
head=0
tail=0
for i in range(Flip_Nos):
	random_value=random()
	if random_value < 0.5:
		head+=1
	else:
		tail+=1

print("Percent Of Head is",head/Flip_Nos*100)
print("Percent Of Tail is",tail*100/Flip_Nos)
