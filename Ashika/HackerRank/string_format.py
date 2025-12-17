def print_formatted(number):
    w=len(f'{number:b}')
    for i in range(1,n+1):
        print(f'{i:{w}d} {i:{w}o} {i:{w}X} {i:{w}b}')
    
   
    # your code goes here
    

if __name__ == '__main__':