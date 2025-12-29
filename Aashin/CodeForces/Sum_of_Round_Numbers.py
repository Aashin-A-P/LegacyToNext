n = int(input())
import math
for i in range(n):
    s = ''
    c = 0
    a = int(input()) 
    div = 10 ** int(math.log10(a))
    while a>0:
        no = a//div 
        no = div * no
        if no!=0:
            s+= str(no)+ " "
            c+=1
        a = a%div
        div = div//10
    print(c)
    print(s)