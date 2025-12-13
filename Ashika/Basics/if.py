price=1000000
credit=True
cre=True
if credit:
    down=0.1*price
elif cre:
    print('You are crediting')
else:
    down=0.2*price
print(f"{down} is the payment")