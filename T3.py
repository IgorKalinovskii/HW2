x=int(input('vvedite god '))
if (((x%4)==0) and ((x%100) != 0)) or (x%400 == 0):
    print('YES')
else:
    print ('NO')

