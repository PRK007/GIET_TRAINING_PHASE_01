
def sumstr(n):
    
    l=[]
    for i in range(len(n)-1):
        for j in range(i+1,len(n)):
            x=n[i:j+1]
            s=0
            for k in x:
                s+=int(k)
            if s==10:
                l.append(x)
    return(l)
           
            
        

n='3523014'
print(sumstr(n))
