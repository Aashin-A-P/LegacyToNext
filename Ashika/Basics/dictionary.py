cus ={
    "name":'ashik',
    "age":10
}
cus["name"]='ashika'
print(cus)
print(cus["name"])
print(cus.get("birth"),'21-01-2005')
phone=input("phone: ")
ans={
    "1":'One',
    "2":'two',
    "3":'three'
}
for c in phone :
    print(ans[c])

greet=input("enter: ")
answ={
    ':)':"😊",
    ':(':"😒"
}
msg=greet.split(" ")
op=''
for word in msg:
    op+=answ.get(word,word)
print(op)
