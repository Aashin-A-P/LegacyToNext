A=[1,17,23,45]
key=23
fl=0
for i in A:
    if(key==i):
        fl=1
        print('found')
        break
if(not fl):
    print('not found')
