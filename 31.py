#local variable and global variabls
#متغیر محلی و متغیر های عمومی

#x, which is inside the body of the function, is called a local variable
#به x که در درون بدنه تابع است متغیر محلی مگویند

#The variable x outside the body of the function is called a public variable
#به متغیر x خارج از بدنه تابع متغیر عمومی میگوییم


x=8   #===> global variable متغیر عمومی
def show():
    x=5   #===> local variable متغیر محلی
    print(x)

show()
print(x)

'''
We can access public variables from within the function, and the opposite is not the case
ما میتوانیم از درون تابع به متغیر های عمومی دسترسی داشته باشیم و لی عکس ان نمیشود

'''