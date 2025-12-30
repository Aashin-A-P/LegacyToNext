def bisearch(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif x>arr[mid]:
            low= mid+1
        else:
            high= mid-1
    return -1
arr=[10,20,30,40,50,60]
x=int(input("Enter the number to search:"))
result=bisearch(arr,x)
if(result==-1):
    print("NOT FOUND")
else:
    print("FOUNDDDD")    
