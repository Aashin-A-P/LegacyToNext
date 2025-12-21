import random

class Dice:
    def roll(self):
        ch=(1,2,3,4,5,6)
        ans1=random.choice(ch)
        ans2=random.choice(ch)
        print(f'{ans1},{ans2}')


di=Dice()
di.roll()

for i in range(3):
    print(random.random())
    print(random.randint(10,20))
