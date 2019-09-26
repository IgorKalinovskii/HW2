a = int(input('введите число A\n'))
b = int(input('введите число B\n'))
c = int(input('введите число C\n'))

if a==b:
    if a==c:
        print('3')
    else:
        print('2')
else:
    if a==c:
        print('2')
    else:
        if b==c:
            print('2')
        else:
            print('0')

