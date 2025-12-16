if __name__ == '__main__':
    s = input()
    val=False
    for char in s:
        if(char.isalnum()):
            val=True
            break
    print(val)
    val=False
    for char in s:
        if(char.isalpha()):
            val=True
            break
    print(val)
    val=False       
    for char in s:
        if(char.isdigit()):
            val=True
            break
    print(val)
    val=False
    for char in s:
        if(char.islower()):
            val=True
            break           
    print(val)
    val=False
    for char in s:
        if(char.isupper()):
            val=True
            break
    print(val)        
    