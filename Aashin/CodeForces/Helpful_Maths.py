a = list(map(int,input().split('+')))
a = sorted(a)
print('+'.join(str(i) for i in a))