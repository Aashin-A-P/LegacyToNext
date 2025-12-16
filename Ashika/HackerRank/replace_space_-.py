def split_and_join(line):
    # write your code here
    ans=line.split(' ')
    res=''
    for i in ans:
        res+=i
        res+='-'
    
    return res[:-1]
        
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)