list = [100,1,55,3,-1,20]
inc = a = b = 0

for i in list:
    if inc == 0:
        a = i
        #b = i
    else:
        if i > a:
            b,a = a,i
            print('a:',a)
            print('b:',b)
        elif i > b:
            b = i
            print('b:',b)
    inc += 1
print('----------------')
print('Biggest:',a,' ','2nd Biggest:',b)