def num(n):
    if(n==1):
        return 1
    
    return n*num(n-1)

nu=int(input())
val=num(nu)
print(val)
