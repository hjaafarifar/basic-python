'''
If we have a condition that may contain several conditions, we use the (elif) command. In this case, 
the conditions are checked one by one, and if they match 
one of the conditions of the desired block, it is executed and the program ends.

اگر ما حالتی داشتیم که ممکن بود شامل چند شرط باشد از دستور 
elif استفاده میکنیم در ای حالت یکی یکی شرطها برسی میشوند و در صورت تطابق با یکی از حالات بلوک مورد نظر اجرا شده و برنامه تمام میشود
'''

score=float(input('enter your score...: '))

if 80<score:
    print('excellent')
elif 60<score<=80:
    print('good')
elif 40<score<=60:
    print('weak')
else:
    print('rejected')