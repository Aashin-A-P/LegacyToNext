salary=int(input("enter salary:"))
age=int(input("enter age:"))
if(salary>=20000 or age<=20):
    loan_amount=int(input("enter loan amount:"))
    if(loan_amount>50000):
        print("max loan amount is 50k")
    else:
        print("you are eligible")
else:
    print("you are not eligible")