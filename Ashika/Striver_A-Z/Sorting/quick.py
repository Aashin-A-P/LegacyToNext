def par(a,l,h):
    pi=a[h]
    i=l-1
    for j in range(l,h):
        if(a[j]<pi):
            i+=1
            a[i],a[j]=a[j],a[i]
    a[h],a[i+1]=a[i+1],a[h]
    return i+1
def quick(a,l,h):
    if(l<h):
        p=par(a,l,h)
        quick(a,l,p-1)
        quick(a,p+1,h)
A=[65,24,12,22,11]
quick(A,0,len(A)-1)
for i in A:
    print(i)