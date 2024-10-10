# mylist=[int(input('Enter num: '))/2 for i in range(5)]
# print(mylist)




mylist=[i==int(input('Enter number: ')) for i in range(5) if i/2==0]
print(mylist)