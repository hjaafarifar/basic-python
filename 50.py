
# Different ways to create a dictionary
# راه های مختلف ایجاد دیکشنری


# Using the (zip) function to convert a double list into a dictionary
# استفاده از تابع (zip) برای تبدیل دولیست به یک دیکشنری
keys=['A','B','C','D']
value=[1,2,3,4]
mydict=dict(zip(keys,value))
print(mydict)


print('*'*50)

# Using the function (dict)
# استفاده از تابع (dict) 
a=dict(v=5,j=True,k='world')
print(a)

print('*'*50)

# Using the fromkeys method function
# استفاده از تابع متد fromkeys
b=dict.fromkeys(range(5),True)
print(b)

