n = int(input())
arr = list(map(int, input().split()))
k=2
    
arr=list(set(arr))  
    
temp=arr.copy()
for i in range(k):
       lar=temp[0]
       for i in temp:
         if i > lar:
          lar=i
       temp.remove(lar)

print("The runner up score is",lar)