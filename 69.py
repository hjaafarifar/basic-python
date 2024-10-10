
# A menu for a better understanding of the program
# یک منو برای درک بهتر برنامه
def menu():
    print('1 student')    
    print('2 employe')
    print('3 Exit...')
    choice=int(input('Select and press enter...: '))
    return choice

# mother class
# کلاس مادر
# In the mother class, the common characteristics of two child classes are present,
# and the two child classes inherit from it
# در کلاس مادر ویژگی های مشترک دو کلاس فرزند امده است و دو کلاس فرزند از ان ارث بری میکنند
class people:
    def __init__(self,code,fname,lname):
        self.code=code
        self.fname=fname
        self.lname=lname
    def __str__(self):
        s='\n code: '+str(self.code)
        s+='\n fname: '+str(self.fname)
        s+='\n lname: '+str(self.lname)
        return s

# In addition to the features of the people class, the student class has a student grade feature and an acceptance function
# کلاس دانش آموز علاوه بر ویژگی های کلاس مردم دارای ویژگی نمره دانش اموز و تابع قبولی است 
class Student(people):
    def __init__(self, code, fname, lname,score):
        people.__init__(self,code, fname, lname)
        self.score=score

    # Checks the student's acceptance function
    # تابع قبولی دانش اموز را برسی میکند
    def ispass(self):
        if self.score>12:
            return 'pass'
        else:
            return'no pass'
        
    # The str function inherits from the People class and then adds the rest of the states to it
    # تابع str  از کلاس مردم ارثبری میکند و سپس بقیه حالات را به ان اضافه میکند
    def __str__(self):
        s=people.__str__(self)
        s+='\n score: '+ str(self.score)
        s+='\n acceptance status: '+str(self.ispass())
        return s
    
        
        
# The employee class remains the student class follows the people class
# کلاس کارمند ماند کلاس دانش آموز از کلاس مردم پیروی میکند 
class Employe(people):
    def __init__(self, code, fname, lname, income):
        people.__init__(self,code, fname, lname)
        self.income=income
        
    # A function that calculates the necessity of paying taxes according to salary
    # تابعی که شرایت پرداخت مالیات را با توجه به حقوق محاسبه میکند
    def tax(self):
        if self.income>1500000:
            return 'must pay taxes'
        else:
            return 'tax free'
    def __str__(self):
        s=people.__str__(self)
        s+='\n income: '+ str(self.income)
        s+='\n tax status: '+ str(self.tax())
        return s





# We have an infinite loop and the program is running until we select the number 3 from the menu
# یک حلقه بی نهایت داریم و تا زمانی که عدد 3 را از منو انتخاب نکرده باشیم برنامه در حاات اجرا قرار دارد 
while 1: 
    chose=menu()
    if chose==3:
        break

    elif chose==1:
        code=int(input('enter code...: '))
        fname=input('first name...: ')
        lname=input('last name...: ')
        score=float(input('enter score...: '))
        mystudent=Student(code,fname,lname,score)
        print(str(mystudent))

    elif chose==2:
        code=int(input('enter code...: '))
        fname=input('first name...: ')
        lname=input('last name...: ')
        income=float(input('enter income..: '))
        myemploye=Employe(code,fname,lname,income)
        print(str(myemploye))
    
    print('*'*50)
    