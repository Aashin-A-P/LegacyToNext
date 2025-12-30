def search(arr,n):
    n=len(arr)
    for i in range(0,n):
        if(arr[i]==x):
            return i
    return -1
arr=[23,24,76,18]
x=int(input("Enter the number to search:"))

result=search(arr,x)
if(result==-1):
      print("element is not present")
else:
      print("element is present")
   