if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))  
    arr.sort(reverse=True)
    uni=[]
    for i in arr:
        if i not in uni:
            uni.append(i)
            
print(uni[1]) 
    