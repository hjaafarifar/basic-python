# A simple class to check the information of a student and check her acceptance in the exam
# کلاس ساده برسی اطلاعات یک دانش آموز و برسی قبولی آن در امتحان

class Student:
    def __init__(self,code,fname,lname,score):
        self.code=code
        self.fname=fname
        self.lname=lname
        self.score=score
    
    def ispass(self):
        if self.score>=12:
            return 'pass'
        else:
            return 'no pass'
    def __str__(self):
        s='\n code= '+   str(self.code)
        s+='\n fname= '+ str(self.fname)
        s+='\n lname= '+ str(self.lname)
        s+='\n score= '+  str(self.score)
        s+='\n Pass the exam: '+str(self.ispass())
        return(s)

a=int(input('Enter code: '))
b=input('Enter fname: ')
c=input('Enter lname: ')
d=float(input('Enter score: '))
student=Student(a,b,c,d)

print(str(student)) 