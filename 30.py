#Simple calculator
#ماشینحساب ساده

def calculate(x,y,op):
    if op=='+':
        print(x , '+' ,y,'=',x+y)
    elif op=='-':
        print(x , '-' ,y,'=',x-y)
    elif op=='*':
        print(x , '*' ,y,'=',x*y)
    elif op=='/':
        print(x , '/' ,y,'=',x/y)
    elif op=='**':
        print(x , '**' ,y,'=',x**y)
    elif op=='%':
        print(x , '%' ,y,'=',x%y)
    else:
        print('operator is not valid...')

a=float(input('Enter number: '))
b=float(input('Enter number: '))
op=input('Enter operator( + , - , / , * , ** , %): ')

calculate(a,b,op)