sum=0
a=[]
for i in range(10):
    num=int(input("enter num:"))
    a.append(num)
print(a)
for i in a:
    sum=sum+i
print(sum)
avg=sum/10
print(avg)