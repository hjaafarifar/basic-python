#Functions in Python are divided into 2 categories. Library functions such as print and functions written by the programmer
#توابع در پایتون به 2 دسته تقسیم میشوند. توابع کتابخانه ای مانند print و توابعی که برنامه نویس مینویسد
'''

def Custom name of the function(parameters):
       The body of the function  

'''


def total(x,y):
    sum=x+y
    print(sum)

a=int(input('Enter number 1: '))
b=int(input('Enter number 2: '))

#In this part, we call the function
#در این قسمت تابع را فراخوانی میکنیم
total(a,b)