def mutate_string(string, position, character):
    lists=[]
    for char in string:
        lists.append(char)
        
    lists[position]=character
    res=''
    for i in lists:
        res+=i
        
    return res

if __name__ == '__main__':