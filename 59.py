try:
    x=int(input('inter x:'))
    y=int(input('inter y:'))
    print(x/y)
    print(x*y)
except ValueError:
    print('value error')
except ZeroDivisionError:
    print('ZeroDivisionError')
except OverflowError:
    print('OverflowError')



