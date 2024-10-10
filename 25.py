#factoriel
#فاکتوریل



number=int(input('Enter your number...:'))
sum=1
while number>1:   
    if number==1 or number==0:
        print('1')
        break
    else:
        sum*=number
        number-=1
print(sum)
