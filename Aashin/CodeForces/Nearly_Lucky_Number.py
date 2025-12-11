n = input()
count = sum(1 for digit in n if digit in '47')

def is_lucky(x):
    return all(d in '47' for d in str(x))

print("YES" if is_lucky(count) else "NO")
