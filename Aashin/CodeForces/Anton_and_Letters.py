a = input()
b = set()
for i in a:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        b.add(i)
print(len(b))