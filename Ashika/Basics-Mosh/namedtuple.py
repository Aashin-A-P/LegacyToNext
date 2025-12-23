from collections import namedtuple
n=int(input())
field=input().split()
Student=namedtuple('Student',' '.join(field))
avg=0
for i in range(n):
    vals=input().split()
    s=Student(*vals)
    avg+=int(s.MARKS)
    
print(avg/n)