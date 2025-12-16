if __name__ == '__main__':
    N = int(input())
    lists=[]
    for i in range(N):
        operation,*line=input().split()
        num=list(map(int,line)) 
        match operation:
            case 'insert':               
                    lists.insert(num[0],num[1])
            case 'print':
                print(lists)
            case 'remove':
                lists.remove(num[0])
            case 'append':
                lists.append(num[0])
            case 'sort':
                lists.sort()
            case 'pop':
                lists.pop()
            case 'reverse':
                lists.reverse()
                
            
            
        