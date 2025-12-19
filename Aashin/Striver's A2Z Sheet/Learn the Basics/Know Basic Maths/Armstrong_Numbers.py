import math
def armstrong(a,nod):
    ab = 0
    while(a>0):
        d = a%10
        a= a//10
        ab+= d**nod
    return ab

n = int(input())
nod = int(math.log10(n)) + 1
print(n == armstrong(n,nod))