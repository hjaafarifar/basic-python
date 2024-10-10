#Combination of (for) loop and conditional statement (if)
#ترکیب حلقه for  و دستور شرطی if

#this program find even number
#این برنامه اعداد زوج را پیدا میکند


a=int(input('enter number 1: '))
b=int(input('enter number 2: '))
if a<=b:
    for i in range(a,b):
        if i%2==0:
           print(i)
else:
    print('a cannot be bigger than b pleas enter corect number... ')
