l=[50,25,10,5]
c=0
s=50
sum1=0
for i in l:
    for k in range(len(l)):
        
        for j in range(s):
            sum1+=j
            if sum1==s:
                c+=1
        else:
            if i+l[k]==s:
                c+=1
            
print(c)        
        
    
        
