//mine
n = int(input())
output=0
j=1
if n>=1:
    for i in range(n,0,-1):
        output+=i*j
        j=j*10
    print(output)

//actual
n = int(input())

if n>=1:
    for i in range(1,n+1):
        print(i,end='')