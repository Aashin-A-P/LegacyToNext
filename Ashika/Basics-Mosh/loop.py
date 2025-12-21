is_car=False

while 1:
    nam=input('enter: ')
    if nam=='start' and not is_car:
        print('start the car')
        is_car=true
    elif nam=='stop' and is_car:
        print('stop the car')
    elif nam=='exit':
        print('exited')
        break
    else:
        print('cannot understand')

price=[20,30,40]
cost=0 
for item in price :
    cost+=item
print(cost)


for item in range(2):
    print('*'*5)
    for item1 in range(item+1):
        print('*'*2)

      