from itertools import permutations 
  
String=input("Enter String For Permutation")
class Permutation:
	def permutationString(val):
		#print(val)
		#print(val)
		permList = permutations(val)
  
		#print all permutations 
		for perm in list(permList): 
			print (''.join(perm)) 
		
Permutation.permutationString(String)
		