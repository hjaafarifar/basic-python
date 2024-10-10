#Program for drawing triangles with stars
#برنامه کشیدن مثلث با ستاره

a=int(input('enter a number: '))
if a>2:
    for i in range(0,a):
        for j in range(0,i+1):
            print('*',end=' ')
        print('\t')
else:
    print('please enter a number bigger than 2...')
    