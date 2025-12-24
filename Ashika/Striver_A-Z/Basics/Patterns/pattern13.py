n=int(input())
count=1
ans=1
for i in range(1,n+1):
    for j in range(0,count):
        print(ans,end=' ')
        ans+=1
    count+=1
    print()
    