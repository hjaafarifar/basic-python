# Indirect inheritance
# ارث بری غیر مستقیم
'''
Suppose we have 3 classes named A, B and C, where class C inherits from class B and class B inherits from class A.
In this case, class C has access to all the attributes
and methods of classes A and B. Class B has access to all attributes and methods of class A

فرض کنید ما 3 کلاس داریم به نام  A و B و C که کلاس C از کلاس B ارث بری میکند 
و کلاس B از کلاس A ارث بری میکند در این صورت کلاس C به تمام صفات 
و متد های کلاس های A و B دسترسی دارد و کلاس B به تمام صفات و متد های کلاس A دسترسی دارد

'''

class A:
    def info1(self):
        print('a')
class B(A):
    def info2(self):
        print('b')
class C(B):
    def info3(self):
        print('c')



# Only access to its own methods and attributes with (.)
# فقط دسترسی به متد ها و صفات خودش با (.)
car1=A()
car1.info1()

print('*'*50)

# Access to its own methods and attributes and class A with (.)
#  دسترسی به متد ها و صفات خودش و کلاس A با (.)
car2=B()
car2.info1()
car2.info2()

print('*'*50)

# Access to own methods and attributes and class A and B with (.)
#  دسترسی به متد ها و صفات خودش و کلاس  A و B با (.)
car3=C()
car3.info1()
car3.info2()
car3.info3()