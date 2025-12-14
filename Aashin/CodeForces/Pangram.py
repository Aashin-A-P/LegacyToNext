n = int(input())
s = input()
if n<26:
    print("NO")
else:
    flag = True
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in s and i.upper() not in s:
            flag = False
            break
    if(flag):
        print("YES")
    else:
        print("NO")