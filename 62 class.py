'''
In the real world, objects have a series of characteristics such as color, weight, name, etc.,
which determine their appearance. These characteristics are called attributes.

در دنیا واقعی اشیا یک سری ویژگی ها از قبیل رنگ، وزن، نام و...
دارند که شکل ظاهری ان ها را تعین میکنند این ویژگی ها صفات نام دارند


In addition to the attributes of a series of behaviors,
these objects show that these behaviors are subject to names

این اشیا علاوه بر صفات یکسری رفتار از خودشان نشان میدهند که این رفتار ها  تابع نام دارند


For example, consider a car, its appearance features such as color, weight, number of doors, etc.
are called attributes or properties of the car class.

مثلا یک اتومبیل را در نظر بگیرید ویژگی های ظاهری ان مانند رنگ، وزن، تعداد در ها و غیره
را صفات یا خواص کلاس ماشین میگوییم

We call the operations of turning on, accelerating, turning on the wipers, etc.
as car class functions

عملیات روشن شدن، سرعت گرفتن، روشن شدن برف پاکن و غیره را توابع کلاس ماشین میگوییم

'''

class Car:
    color='red'
    doors=4
    def start_engine(self):
        print('engine is started...')

# Create an object of a class
# ساختن یک شی از کلاس 
mycar=Car()
print(mycar.doors)
print(mycar.color)
mycar.start_engine()

# If we print the object type, it will tell us that it is of the car class
# اگر نوع شی را چاپ کنیم به ما میگوید که از کلاس ماشین است
print(type(mycar))

# In the code above (doors, color) are the attributes of our class and (start engine) is the method of our class.
# در تکه کد بالا (doors , color) صفت های کلاس ما هستند و (start engine) متد کلاس ما میباشد.

# self is a Python keyword here and should be written by default in functions,
#  we will learn more about it in the future
# self در اینجا یک کلمه کلیدی پایتون است و باید در توابع به صورت پیش فرض نوشته شود
#  در اینده بیشتر با ان اشنا میشویم

'''
By using the internal function (isinstance), you can find out what class the object we have is of
با استفاده از تابع درونی (isinstance) میتوان فهمید که ابجکتی که داریم از نوع چه کلاسی است

print(ininstance(object name,class name))
'''