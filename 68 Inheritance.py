'''
Inheritance in classes means that, for example, we have a class called
the People class, where the student and employee classes can follow the
People class because all students and employees are human and have the
same characteristics, for example, all students and Employees have first
and last names, which can be derived from the People class. 
We will understand the issue better by examining a few pieces of code.

وراثت در کلاس ها به این معنا میباشد  برای مثال ما کلاسی به اسم کلاس
مردم داریم که کلاس های دانش آموز و کارمند میتوانند از کلاس مردم پیروی کنند 
چون همهی دانش اموزان و کارمندان انسان هستند و دارای ویژگی های یکسان هستند
مثلا همه دانش اموزان و کارمندان دارای نام و نام خانوادگی هستند که میتوانند 
از کلاس مردم مشتق شوند در ادامه با برسی چند قطعه کد بهتر متوجه موضوع میشویم

'''
# Class A is the parent class here
# کلاس A در اینجا کلاس پدر است
class A:
    def myfA(self):
        print('hello world!...')
    def sumA(self):
        print(5+15)


# Class B is the child class here
# کلاس B در اینجا کلاس فرزند است
# Note that for inheritance, we must put the name of the parent class in parentheses in front of the parent class when defining the child class.
# توجه کنید که برای ارث بری باید نام کلاس پدر را در هنگام تعریف کلاس فرزند در پرانتزی مقابل کلاس فزرند بیاوریم
class B(A):
    def myfB(self):
        print('Class B is the inheritor of class A...')
    

# After creating an object from the child class, we can access the methods and attributes of the parent class with (.)
# پس از ایجاد یک شی از کلاس فرزند میتوانیم با ( . ) به متد ها و صفات کلاس پدر نیز دسترسی داشته باشیم

myobjectB=B()   
myobjectB.myfA()
myobjectB.myfB()
myobjectB.sumA()


# But if we create an object from the parent class (A), we only have access to the attributes and methods of the parent class
# اما در صورت ساخت شی از کلاس پدر(A) فقط به صفات و متد های کلاس پدر دسترسی داریم
myobjectA=A()
myobjectA.myfA()
myobjectA.sumA()
