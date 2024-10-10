#This program gets the number of letters in a string
#این برنامه تعداد حروف یک رشته را به دست می اورد

a=input('enter your text...: ')
x=0
for i in a:
    
    if i!=' ':#If it comes to the space between words, because we have used the opposite sign, it does not count the space as a letter.
              #در صورتی که به فاصله بین  کلمات میرسد چون از علامت مخالف استفاده کرده ایم خط فاصله را به عنوان حرف حساب نمیکند   
        x+=1
print(x)