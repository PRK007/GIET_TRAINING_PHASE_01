w1='iii'
w2='i'
l1=list(w1)
l2=list(w2)
l3=[]

for i in l1:
    if i in l2 and i!=' ' and (i not in l3):
        l3.append(i)


print("".join(l3))
