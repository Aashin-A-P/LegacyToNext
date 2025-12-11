t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    iterations = 0
    while True:
        idx1 = next((i for i in range(n) if a[i] > b[i]), None)
        if idx1 is not None:
            a[idx1] -= 1
        else:
            iterations += 1
            break
        
        idx2 = next((i for i in range(n) if a[i] < b[i]), None)
        if idx2 is not None:
            a[idx2] += 1
        
        iterations += 1
    
    print(iterations)
