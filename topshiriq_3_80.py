
x=int(input("kiriting x="))
i=0
s=0
n=0
def faktorial(n):
    res = 1
    for c in range(1, n +1):
     res *= c
    return res
for c in range(1, n+1):
    pass
while n<=13 and i<=10:
    i=i+1
    n=2*i+1
    if i%2==1 :
        a=-1
    else:
        a=1
    y=x**(n)/(faktorial(n))
    s=s+y*a
    
print('yigindi:' , s)   



