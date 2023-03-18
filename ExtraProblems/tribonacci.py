
n=10
n1=0
n2=1
n3=1
s=n3+n2+n1
for i in range(1,n-3):
    n1,n2,n3=n2,n3,s
    s=n1+n2+n3
print(s)    
    
    
