lst=[100,89,3,67,123,220]
k=2
temp=lst.copy()
for i in range(k):
  lar=lst[0]
  for i in temp:
    if i > lar:
        lar=i
  temp.remove(lar)

print(lar)
