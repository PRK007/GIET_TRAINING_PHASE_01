"""  Given a number n, write a program to find the sum of the largest prime factors of each of nine consecutive numbers starting from n.
g(n)=f(n)+f(n+1)+f(n+2)+f(n+3)+f(n+4)+f(n+5)+f(n+6)+f(n+7)+f(n+8)
where, g(n) is the sum and f(n) is the largest prime factor of n
for example,
g(10)=f(10)+f(11)+f(12)+f(13)+f(14)+f(15)+f(16)+f(17)+f(18)
     =5+11+3+13+7+5+2+17+3
     =66  """

def isprime(i):
    for k in range(2,i-1):
        if i%k==0:
            return False

    return True

def func(n):
    for i in range(n,1,-1):
        if ( isprime(i) and n%i==0):
            return i
        
    
s=0
n=int(input())
for p in range(n,n+9):
    s+=func(p)
print(s) 

