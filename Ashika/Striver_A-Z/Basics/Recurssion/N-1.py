def num(n):
    if(n==0):
        return 0
    
    print(n)
    return num(n-1)

nu=int(input())
num(nu)