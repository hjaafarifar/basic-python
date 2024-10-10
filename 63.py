class Car:
    color='red'
    doors=4
    def start_engine(self):
        print(f'The engine of the car with the ***{self.doors}*** door and ***{self.color}*** color is bright')
        #(f string) helps us to use the variables anywhere in a string data, it is enough to first put an f in the desired string,
        # then add the variables in curly brackets in the desired place
        # (f string) به ما کمک میکند که متغیر ها را در هر کجای یک داده رشته ای به کار ببریم
        # کافی است که اول رشته مورد نظر یک f قرار دهیم سپس متغیر ها را درون کرلی براکت در جای دلخواه اضافه کنیم
    
mycar=Car()

# We can assign class attributes outside the class and change them
# ما میتوانیم صفت های کلاس را خارج از کلاس مقدار دهی کنیم و ان ها را تغییر دهیم 
# Of course, we will learn how to lock adjectives later
# البته در ادامه با نحوه قفل کردن صفت ها اشنا میشویم
mycar.color='black'
mycar.doors=2

print(mycar.color)
print(mycar.doors)
mycar.start_engine()