#A list can be sorted by using the sort method. If all members of the list are of the same data type
#با استفاده از متد (sort) میتوان یک لیست را مرتب کرد. در صورتی که تمام اعضای لیست از یک نوع داده ای باشند


mylist=[1,15,5,6,48,1,63,87,52,2,3]
mylist.sort()
print(mylist)


print('*'*50)


#If we want the list to be sorted from big to small, we do as follows
#اگر بخواهیم لیست از بزرگ به کوچک مرتب شود به صورت زیر عمل میکنیم
mylist.sort(reverse=True)
print(mylist)

print('*'*50)

'''
   The inner function (sorted) sorts the list like the sort method,
   with the difference that the sort method modifies the original list,
   while the sorted function creates a new list.

   تابع درونی (sorted) مانند متد sort لیست را مرتب میکند
     با این تفاوت متد sort خود لیست اصلی را اصلاح میکند 
   در حالی که تابع sorted یک لیست جدید ایجاد میکند 
'''

mylist2=['h','r','a','w']
print(sorted(mylist2))