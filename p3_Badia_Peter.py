#iterating over a string passed to the function to find duplicates or letters
#then printing the duplicates
#i = index and j = letter tested and compared to i
def find_dup_str(s,n) :
    for i in range (len(s)-n+1) :
        for j in range(i+1,len(s)-n+1) :
            if s[i:i+n]==s[j:j+n] :
                return(s[i:i+n]) 

#function iterating over a string finding the largest duplicated string in a 
#string given by the user
def find_max_dup(s) :
    max_dup=""
    for n in range (1,len(s)//2+1) :
        dup=find_dup_str(s,n)
        
        if dup!="" :
            max_dup=dup
        return max_dup
    
#requesting unput from the user

s=input('Enter a string:')
n=int(input('enter string length to check'))
#callingt he funcctions
substring=find_dup_str(s, n)
print(substring)
max_dups=find_max_dup(s)
print(max_dups)
