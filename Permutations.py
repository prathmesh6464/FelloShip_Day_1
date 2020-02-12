#Function for generating different permutations of the string  
def generatePermutation(string,start,end):  
    current = 0;  
    #Prints the permutations  
    if(start == end-1):  
        print(string);  
    else:   
        for current in range(start,end):  
  
       #Swapping the string by fixing a character  
            x = list(string);  
            temp = x[start];  
            x[start] = x[current];  
            x[current] = temp; 
      #Recursively calling function generatePermutation() for rest of the characters  
  
            generatePermutation("".join(x),start+1,end);  
            #Swapping the string by fixing a character  
            temp = x[start];  
            x[start] = x[current];  
            x[current] = temp;  
  
str = input("Enter String For Permutations : ")
n = len(str);  
print("All the permutations of the string are: ");  
generatePermutation(str,0,n);