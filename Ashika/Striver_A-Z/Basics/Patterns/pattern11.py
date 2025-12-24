n=int(input())

for i in range(1,n+1):
    if(i%2==0):
        a=0
        for j in range(1,i+1):
            print(a,end='')
            if(a==0):
                a=1
            else:
                a=0
            
        
    else:
        a=1
        for j in range(1,i+1):
            
            print(a,end='')
            if(a==1):
                a=0
            else:
                a=1
    print()
  

        

    