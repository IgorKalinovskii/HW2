a = int(input('введите число A\n'))
b = int(input('введите число B\n'))
c = int(input('введите число C\n'))

if ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
    print('YES')
else:
    print('NO')

