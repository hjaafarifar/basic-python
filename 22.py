#Calculate the factorial of a number
#محاسبه فکتوریل یک عدد


number=int(input('enter your number:'))

#A variable to put the factorial value in it
#متغیری برا ریختن مقدار فاکتوریل در ان
fact=1   
for i in range(1,number+1):
    fact*=i
print(fact)