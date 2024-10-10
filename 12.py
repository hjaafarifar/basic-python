# Sorting 3 input numbers with if statement
# مرتب کردن 3 عدد ورودی با 1 دستور if  2 31

# Getting input
# گرفتن ورودی
a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
c = int(input('Enter number 3: '))


#Using the logical operator (and) To compare numbers
#استفاده از عملگر منطقی (and) برای مقایسه اعداد

if a > b and b > c:
    print(c ,'<', b ,'<', a)
elif a>c and c>b:
    print(b ,'<', c ,'<', a)
elif b>c and c>a:
    print(a ,'<', c ,'<', b)
elif b > a and a > c:
    print(c ,'<', a ,'<', b)
elif c > a and a > b:
    print(b ,'<', a ,'<', c)
elif c>b and b>a:
    print(a ,'<', b ,'<', c)
