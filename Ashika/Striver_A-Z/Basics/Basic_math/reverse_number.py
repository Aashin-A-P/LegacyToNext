n=int(input())
ans=0
while(n!=0):
    dig=n%10
    ans+=dig
    ans*=10
    n=n//10
    
ans//=10   
print(f'Reverse of number:{ans}')