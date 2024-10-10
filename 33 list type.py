'''
The general form of the list is as follows, and its elements are placed in two brackets, 
which can include any number, string, list, etc.

شکل کلی لیست به صورت زیر است و عناصر ان درون دو براکت قرار میگیرند که میتواند
 شامل هر اعداد، رشته، لیست و ... باشد باشد

'''
list1=[[1,'g'],5,9,"hello",True]
print(type(list1))



#You can use step and cut in lists
#در لیست ها میتوان از گام و برش استفاده کرد
print(list1[2:4])




#Each member of your lists is an index that can be used to reach the desired element of the list. Indexes in lists start from zero.
#هر عضو از لیست ها داری یک شاخص است که میتوان با ان به عنصر مورد نظر لیست دست پیدا کرد شاخص در لیست ها از صفر شروع میشود
print(list1[3])