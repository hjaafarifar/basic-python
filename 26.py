#This program returns three-digit numbers that are divisible by the sum of 3 digits
#این برنامه اعداد سه رقمی که بر مجموع 3 رقم خود بخش پذیر هستند را برمیگرداند

for i in range(101,1000,2):
    n=i

    #A variable that stores the sum of three digits
    #متغیری که مجموع سه رقم را در خود ذخیره میکند
    sum=0
    while n>0:
        sum+=n%10

        #The // operator gives us the correct remainder
        #عملگر // باقیمانده صحیح را به ما میدهد
        n=n//10
    if i%sum==0:
        print(i,end='\t')