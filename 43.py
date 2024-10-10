'''
Suppose we have a list of tuples, each tuple has two members,
and we want to add the second member to a new list.

فرض کنید لیستی از تاپل ها داریم که هر تاپل دو عضو دارد و میخواهیم 
عضو دوم را به لیست جدیدی اضافه کنیم به صورت زیر عمل میکنیم
'''



mylist=[('num1',1),('num2',2),('num3',3)]
mylist2=[]
for item in mylist:
    mylist2.append(item[1])
print(mylist2)