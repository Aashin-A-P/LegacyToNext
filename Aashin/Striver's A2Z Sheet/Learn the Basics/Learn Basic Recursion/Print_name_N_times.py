def print_name(name,n):
    if n==0:
        return
    print(name)
    print_name(name,n-1)

n = int(input())
name = 'Aashin'
print_name(name,n)