#The command (return) is used to return the value of a function
#دستور (return) برای باز گرداندن مقدار یک تابع به کار میرود

def squrae(x):
    return x**2

a=int(input('Enter number: '))

#Functions that use the (return) command to return the answer, we must use the (print) function to see the final answer
#توابعی که از دستورreturn برای بازگرداندن جواب استفاده میکنند برای دیدن جواب نهایی باید از تابع print استفاده کنیم
print('squrae(',a,')=',squrae(a))