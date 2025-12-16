def count_substring(string, sub_string):
    sums=0
    ls=len(string)
    lss=len(sub_string)
    for i in range(ls-lss+1):
        a=i
        if(string[i]==sub_string[0]):
            ans=0
            for j in range(lss):
                if(string[a]==sub_string[j]):
                    ans+=1
                    a+=1
                else:
                    break
            if(ans==len(sub_string)):                
                sums+=1
                                  
    return sums

if __name__ == '__main__':