# name(can be enything)=[exprestion  for item in (available data)]
mylist=[i for i in range(20) if i%3==0]
print(mylist)

print('*'*50)


mylist1=[('a',15),('b',4),('c',9),('y','world')]
answer=[a[1] for a in mylist1]
print(answer)