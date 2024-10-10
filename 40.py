'''
The purpose of this program is to learn about the internal function 
(len) and change each member of the list

هدف از ای برنامه اشنایی با تابع درونی 
(len) و تغییر هر عضو از لیست است 

'''
# A function that checks the list and changes the desired item if it exists in the list
# تابعی که لیست را چک میکند و آیتم مورد نظر را در صورت وجود در لیست تغییر میدهد
def chenge(item,mylist):

    # The (len) function returns the length of a list to us, after that we can move on it with the for loop and get the indexes.
    # تابع (len) طول یک لیست را برای ما باز میگرداند بعد از ان میتوانیم با حلقه for روی ان حرکت کنیم و ایندکس ها را به دست اوریم
    for i in range(len(mylist)): 

        # mylist[index]=enything
        # نام لیست[index]=هزچیزی
        if mylist[i]==item:
            mylist[i]=True
        else:
            mylist[i]=False
    return mylist
    

mylist=[1,'h',9,'s',7,'q',9,8,'e',9]
item=9
print(chenge(item,mylist))


# In the above code, wherever the desired item is in our list, it sets it to (true) and sets the value to (false).
# در کد فوق هر جا در لیست آیتم ما مورد نظر ما وجود داشته باشد ان را برابر (true) قرار میدهد و بقه را برابر (false) قرار میدهد