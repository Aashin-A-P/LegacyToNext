a =[1,2,3,4,5,4,3,2,5,6,7,2]
d = dict()
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i] = 1
print(d)