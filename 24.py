#When the (while loop) is equal to 1 or true, it means that the loop will be executed until the condition is met
#وقتی حلقه while برابر 1 یا true قرار بگیرد یعنی تا زمانی که شرط برقرار باشد حلقه اجرا میشود

sum=0
while 1:
    a=int(input('inter number: '))
    if a==0:

        #The break command ends the program if the condition is not met
        #دستور break اگر شرط مخالف باشد به برنامه پایان میدهد
        break
    else:
        sum+=a
print(sum)


#This program takes an unknown number of numbers from the user and adds them together. If the entered number is equal to zero, the program ends.
#این برنامه تعداد نامشخصی عدد را از کاربر میگیرد و با هم جمع میکند در صورتی که عدد وارد شده برار صفر باشد برنامه پایان میابد

