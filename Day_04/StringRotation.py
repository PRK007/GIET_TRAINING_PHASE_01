"""string rotation
input: rhdt:246, ghftd:1246
Expl: here every string is associated with the number sep by:
--> if sum of squares of digits is even then rotate the string by 1
--> if sum of squares of digits is odd is odd then rotate the string left by 2 position
2*2+4*6*6=56 which is even so rotate rhdt=trhd

1*1*2*2*4*4*6*6=57 which is odd so rotate left by 2: ghftd=ftdgh  """


s=input().split(",")
stt=[]
numm=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    num.append(n)
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(numm)):
    print(rotate(stt[i],numm[i]))