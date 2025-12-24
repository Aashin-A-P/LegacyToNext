n=int(input())
a=0

for i in range(n,0,-2):
    space=' '*a
    print(space+'*'*i,end='')
    print()
    a+=1
    
