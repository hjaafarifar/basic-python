
a=int(input('enter a number: '))
if a>2:
    for i in range(0,a):
        for j in range(i,a):
            print('*',end=' ')
        print('\t')
else:
    print('please enter a number bigger than 2...')
    