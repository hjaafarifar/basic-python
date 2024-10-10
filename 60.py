def isprimaly(n):
    for i in range(2,n):
        if n%i==0:
            return False
        
    # From the first line until here, the function is to check the oddness of the numbers   
    # از خط اول تا اینجا تابع برسی فرد بودن اعداد است
    return True

# The variable to continue or not continue the loop, if it is true, it will continue, but if it is false, it will not continue
#متغیر برای ادامه یا ادامه ندادن حلقه اگر trueبود ادامه میدهت ولی اگر false بود ادامه نمیدهد
tryagain=True
while tryagain:
    try:

        # The value must be a number, otherwise the next line will be executed
        #مقدار value حتما باید عدد باشد در غیر ای ضورت خط بعدی اجرا میشود
        value=int(input('inter num: '))
    except ValueError:
        print('you mast type number')
        try:
            doOver=input('try again(y or n)?')
        except:
            print('ok see you next time')
            tryagain=False
        else:
            if str.upper(doOver)=='N':
                tryagain=False
    except KeyboardInterrupt:
        print('you press ctrl+c')
        print('see you next time')
        tryagain=False
    else:
        for i in range(2,value+1):
            if isprimaly(i)==True:
                print(i,end='\t')
        tryagain=False
# If ctrl + c is entered, it goes to line 20, which is for entering ctrl c-15f
#در صورتی که  ctrl + c  وارد شود به خط 20 میرود که مختص وارد کردن ctrl c است-15f