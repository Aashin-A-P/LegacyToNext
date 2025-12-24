n=int(input())
real=n
ans=0
while(n!=0):
    dig=n%10
    ans+=dig
    ans*=10
    n=n//10
ans//=10   

if(ans==real):
    print(f'{real} is palindrome')
else:
    print('not palindrome')