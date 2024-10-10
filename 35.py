#Using the pop method, we can give the index of an item from the list and delete it.
#با استفتده از متد (pop) میتوانیم ایندکس یک غضو از لیست را داده و ان را حذف کنیم

mylist=[1,15,'h',['a',5,True],False]
mylist.pop(3)
print(mylist)



#With the use of the (remove) method, we can add and remove a member from the list
#با استفتده از متد (remove) میتوانیم  یک عضو از لیست را داده و ان را حذف کنیم

mylist.remove(15)
print(mylist)

print('*'*50)

#Using the (clear) method, all members of a list are removed and an empty list is returned.
#با استفاده از متد (clear) تمام اعضای یک لیست حذف شده و یک لیست خالی باز میگرداند.

mylist.clear()
print(mylist)