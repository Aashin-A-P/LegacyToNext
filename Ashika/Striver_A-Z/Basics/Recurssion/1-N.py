def num(n):
    if(n==0):
        return 0
    else:
         num(n-1)
         print(n)
        

nu=int(input())
num(nu)