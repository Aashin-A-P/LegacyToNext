income=True
credit=False
crime=False
if income and credit:
    print('Can vote')

elif income or credit:
    print('cannot vote')
else:
    print("completed")
if not crime:
    print('Good person')

else:
    print("completed")