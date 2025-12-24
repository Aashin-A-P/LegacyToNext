n=int(input())
dup=n
d=0
ans=0
while(dup!=0):
    r=dup%10
    d+=1
    dup//=10

dup=n  
while(dup!=0):
    r=dup%10
    ans+=(r**d)
    dup//=10
if(ans==n):
    print('Armstrong number')
    
else:
    print('Not armstrong')
    
    