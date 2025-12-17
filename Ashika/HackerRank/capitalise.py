def solve(s):
    res=s.split(' ')
    ans=[]
    for i in res:
        if(i and i[0].isalpha())         
            ans.append(i.title())
            
        else:
            ans.append(i)
    
    return ' '.join(ans)

if __name__ == '__main__':