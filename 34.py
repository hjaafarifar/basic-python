# Adding a member to the list is done with the append command
#اضافه کردن عضو به لیست با دستور apend انجام میشود

mylist=[1,15,'h',False]
mylist.append(8)
print(mylist)

print('*'*50)

mylist.append('g')
print(mylist)


print('*'*50)

# Adding a member to the list at the desired location is done with the (insert) command
# اضافه کردن عضو به لیست به مکان دلخواه با دستور (insert) انجام میشود

mylist.insert(3,'GOOGLE')
print(mylist)