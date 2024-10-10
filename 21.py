#This program takes a string from the user and reverses it
#این برنامه رشته ای را از کاربر گرفته و ان را معکوس میکند

mystring=input('enter your string: ')
revers_string=''
for i in mystring:
    revers_string=i+revers_string
print(revers_string)