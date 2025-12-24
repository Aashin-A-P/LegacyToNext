x=int(input())
y=int(input())
if(x>y):
    a,b=x,y
else:
    a,b=y,x
while(a!=0 and b!=0):
    a,b=b,a%b
    
print(a)
    