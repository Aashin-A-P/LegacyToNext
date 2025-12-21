n=int(input())
a,b=0,1
if(n==0):
    print(n)
elif(n==1):
    print(n)
else:
    for i in range(2,n+1):
        a,b=b,a+b

print(b)
