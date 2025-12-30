arr = list(map(int,input("Enter the array: ").split()))
key = int(input("Enter key to search: "))
arr = sorted(arr)
lb = 0
ub = len(arr) - 1
flag = False
while lb <= ub:
    m = (lb + ub)//2
    if arr[m] == key:
        print("Element found in pos: ", m)
        flag = True
        break
    elif arr[m] > key:
        ub = m-1
    else:
        lb = m+1
if (not flag):
    print("Element not found")
