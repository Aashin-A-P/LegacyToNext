n=int(input())
lists=[]
for i in range(1,n+1):
    if(n%i==0):
        lists.append(i)
        
print(lists)