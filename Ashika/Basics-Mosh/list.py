numbers=[10,50,50,20,90,80]
max=numbers[1]
print(numbers)
print(numbers[2])
print(numbers[2:4])
numbers.append(100)
print(numbers)
numbers.insert(1,55)
print(numbers)
numbers.remove(55)
print(numbers)
numbers.pop()
print(numbers)
numbers.index(90)
print(numbers)
print( 50 in numbers)
print(numbers)
numbers.count(50)
print(numbers)
numbers.sort()
print(numbers)
numbers2=numbers.copy()
print(numbers2)
numbers.reverse()
print(numbers)
uniq=[]
for uni in numbers:
    if uni not in uniq:
        uniq.append(uni)
for item in numbers:
    if item>max:
        max=item
print(max)
lis=[[1,2,3],[4,5,6]]
for row in lis:
    for col in row:
        print(col)
