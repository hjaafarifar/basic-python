def total(x,y):
    return x+y
x=int(input('Enter number: '))
y=int(input('Enter number: '))

# (assert) I handled a sample error
# یک نمونه هندل کردم خطا  
assert y>x ,'y sholdbe  bigger than x'
print(total(x,y))