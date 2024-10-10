'''

This program takes two numbers and moves them together.
The purpose of this program is to learn the learning function of one of the techniques of moving in Python.

این برنامه دو عدد را گرفته و ان هار را با هم جابه جا میکند هدف از این برنامه
اعلاوه بر یادگیری تابع آموزش یکی از تکنیک های جابه جایی در پایتون است

'''
def swap(x,y):
    x,y=y,x
    return(x,y)
a=int(input('Enter number A: '))
b=int(input('Enter number B: '))
a,b=swap(a,b)
print('A=',a,'\t','B=',b)


'''
a=20
b=50
(a,b=b,a) ===> a=50,b=20

'''
