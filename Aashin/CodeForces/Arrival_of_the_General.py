n = int(input())
a = list(map(int,input().split()))
maxi = max(a)
mini = min(a)
b = a.index(maxi)
c = len(a) - a[-1::-1].index(mini) - 1
if(b<c):
    print(b+(n-c-1))
else:
    print(b+(n-c-2))