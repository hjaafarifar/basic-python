# This piece of code takes the length and width of a rectangle
# from the user and calculates its area and perimeter
# این قطعه کد طول و عرض یک مسطتیل را از کاربر گرفته و مساحت و محیط ان را حساب میکند


# Getting to know the str method in classes
# اشنایی با متد str در کلاس ها

class Rectangle:
    def __init__(self,x,y):
        self.length=x
        self.width=y
    def area(self):
        return self.length*self.width
         
    def perimeter(self):
        return 2*(self.length+self.width)
        

    def __str__(self):
                        # Be sure to use the str keyword for the rest of the data types in the str method
                        # حتما باد از کلمه کلیدی str برای بقیه نوع های داده ای در متد str استفاده کنیم
        s='\n lenhth= '+str(self.length)
        s+='\n width= '+str(self.width)
        s+='\n area= '+ str(self.area())
        s+='\n peramet='+str(self.perimeter())
        return s

x=int(input('Enter length= '))
y=int(input('Enter width= '))
rectangle=Rectangle(x,y)
print(str(rectangle))
