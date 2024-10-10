# This piece of code takes the radius of the circle from the user and calculates the area
# این قطعه کد شعاع دایره را از کاربر گرفته و مساحت را مساحبه میکند

# Constructor method in classes
# متد سازنده در کلاس ها

# The math library is a standard byton library that provides access to math functions in byton.
# To call a library, the import keyword is used
# کتابخانه ریاضی یک کتابخانه استاندارد ‍‍‍‍‍‍‍بایتون است که امکان دسترسی به توابع ریاضی در بایتون را فراهم میکند.
# برای فراخوانی  یک کتابخانه از کلمه کلیدی import استفاده میشود
import math
class Circles_Area:
    pi=math.pi

    # The (init) method is the constructor of the classes,
    # which can be used to take input from the user and use it for calculations inside the class
    # متد (init) سازنده کلاس هاست که از این طریق میتوان از کاربر ورودی گرفت
    # و از ان برای محاسبات داخل کلاس استفاده کرد
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f'area of circle with {self.radius} radius is {self.pi*self.radius**2}')


a=int(input('Enter radius: '))


# Define the input variables for the class by placing them in parentheses in front of it
# تعریف متغیر های ورودی برای کلاس با قرار دادن ان ها در برانتز جلوی ان
mycirclce=Circles_Area(a)
print(mycirclce.pi)
print(mycirclce.radius)
mycirclce.area()
