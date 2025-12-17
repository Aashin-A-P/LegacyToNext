stri=input()
p=input()
ans=0
val=False
num1,num2=map(int,stri.split(' '))
m=p.split('+')
for i in m:
    res=eval(i.replace('x',str(num1)))
    ans+=res
if(ans==num2):
    val=True
    
print(val)
