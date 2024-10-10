#A function that calls itself within itself is called a return function
#به تابعی که خود را درون خودش صدا میزند تابع بازگشتی میگویند


def faktorial(x):
    if x==1 or x==0:
        return 1
    else:
        return x*faktorial(x-1)
    


a=int(input('Enter your number: '))
print(faktorial(a))