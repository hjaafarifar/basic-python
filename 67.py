# Concealment
# پنهانسازی


'''
Sometimes we don't want people who use our program to have access to some of its data,
in this case we have to make the desired data unavailable. 
We do this by using two underlines before the desired data.

گاهی اوقات ما نمیخواهیم که افرادی که از برنامه ما استفاده میکنند به بعضی از داده های ان دسترسی داشته باشند
در این حالت باید داده مورد نظر را از حالت دسترس خارج کنیم
این کار را با استفاده از دو تا اندرلاین قبل از داده مورد نظر انجام میدهیم

'''
class Point:
    # In this piece of code, the data y is from an element that no one can change or even access it
    # در این قطعه کد داده y را از یک عنصر است که کسی نمیتواند ان را تغیر دهد و حتی به ان دسترسی داشته باشد
    __y=51
    def __init__(self,x):
        self.x=x
        
    
    def sum(self):
        return self.x+self.__y
    
mypoint=Point(10)

print(mypoint.x)
print(mypoint.sum())

# By executing the following code, an error message will be printed
# با اجرای کد زیر پیغام خطا چاپ میشود
print(mypoint.__y)
