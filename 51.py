# If we give a new value to a key, it replaces the old value
# اگر مقدار جدیدی به یک کلید دهیم جایگزین مقدار قدیمی میشود


# To add a new value key to the dictionary, proceed as follows
# برای اضافه کردن کلید مقدار جدید به دیکشنری به صورت زیر عمل میکنیم
mydict={'a':1,'b':True,'c':3,'list':['g',2,'A']}
mydict['d']='Hello world'
print(mydict)


print('*'*50)

# The (keys) method displays the keys of a dictionary
# متد(keys) کلید های یک دیکشنری را نمایش میدهد
print(mydict.keys())


print('*'*50)

# The (values) method displays the values ​​of a dictionary
# متد(values) مقدار های یک دیکشنری را نمایش میدهد
print(mydict.values())


print('*'*50)

# The (items) method displays the keys and values ​​of a dictionary in the form of a list
# متد(items) کلید ها و مقدار های  یک دیکشنری را در قالب یک لیست نمایش میدهد نمایش میدهد
print(mydict.items())


print('*'*50)


print(mydict.get('list'))