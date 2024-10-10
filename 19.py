#Find the number of a specific word in a string
#پیدا کردن تعداد یک حرف خاص در یک رشته

a=input('enter your text...: ')
b=input(('Enter the word you want to find...: '))
x=0
for i in a:
    if i==b:
        x+=1 # x is used as a counter here and adds one if the condition is met
             # x در اینجا به عنوان شمارنده به کار میرود و در صورت بر قرار بودن شرط یکی به ان اضافه میکند
print(x)