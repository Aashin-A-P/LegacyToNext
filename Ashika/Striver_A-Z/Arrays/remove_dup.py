A=[1,1,17,17,23,45]
uniq=[]
for i in A:
    if(i not in uniq):
        uniq.append(i)
for i in uniq:
    print(i)
        