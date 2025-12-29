l = list(map(int,input().split()))
print("List: " , l)
key = int(input("ENTER THE KEY TO BE SEARCHED: "))
for i in range(len(l)):
    if l[i] == key:
        print("Element found at Position : " , i )
if i>=len(l):
    print("Element not found")