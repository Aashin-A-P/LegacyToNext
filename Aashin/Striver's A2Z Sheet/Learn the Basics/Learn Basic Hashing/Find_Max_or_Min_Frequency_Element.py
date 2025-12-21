a =[1,2,3,4,5,4,3,2,5,6,7,2]
d = dict()
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i] = 1
maxi = 0
max_elem = a[0]
min_elem = a[0]
mini = 999
for i in d.keys():
    if a[i] > maxi:
        maxi = a[i]
        max_elem = i
    elif a[i] < mini:
        mini = a[i]
        min_elem = i
    else:
        if i < max_elem:
            max_elem = i
        if i < min_elem:
            min_elem = i
print(max_elem)
print(min_elem)