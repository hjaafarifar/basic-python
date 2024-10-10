'''
Using the following piece of code, we can insert an element from the desired 
list and remove all its repetitions from the list

با استفاده تکه کد زیر میتوانیم یک عنصر از لیست مورد نظر وارد کرده
 و تمام تکرار های ان را از لیست حذف کنیم
'''

#Member delete function
def dell(item,mylist):
    for i in mylist:
        if str(i)==item:
            mylist.remove(i)
    return mylist


#List and input
list1=[1,8,'g',8,'s','a',9,4,'r','g',8]
print(list1)
item=input('Enter the item you want to remove from the list...: ')

#Call the function to execute
print(dell(item,list1))

