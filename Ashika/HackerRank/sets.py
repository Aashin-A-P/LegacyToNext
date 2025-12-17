def average(array):
    ans=list(set(array))
    
    sums=0
    for i in ans:
        i=int(i)
        sums+=i
    val=(sums)/len(ans)
    return val
    # your code goes here

if __name__ == '__main__':