def ispalindrome(i):
    s=0
    k=i
    while i>0:
        r=i%10
        s=s*10+r
        i=i//10
    if s==k:
        return True
    else:
        return False
    
def near_palindrome(n):
    i=n+1    
    while(True):
        
        if ispalindrome(i):
            return(i)
        
     
        i=i+1
n=1221
print(near_palindrome(n))
