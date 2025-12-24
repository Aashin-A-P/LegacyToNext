def rev(n,s=0,e=None):
    if(e is None):
        e=len(n)-1
    if(s>=e):
        return 
    n[s],n[e]=n[e],n[s]
    rev(n,s+1,e-1)
    
n=input()
a=n
val=list(n)
rev(val)
ans=''.join(val)
if(ans==n):
    print('Palindrome')
else:
    print('Not palindrome')