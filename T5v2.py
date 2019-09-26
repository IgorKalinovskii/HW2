a = int(input('введите число A\n'))
b = int(input('введите число B\n'))
c = int(input('введите число C\n'))
if a>b:
    if b>c:
        a,b,c = c,b,a
    else:
        if a>c:
            a,b,c = b,c,a
        else:
            a,b,c = b,a,c
else:
    if a>c:
        a,b,c = c,a,b
    else:
        if b>c:
            a,b,c = a,c,b
        else:
            a,b,c = a,b,c
print(a,b,c)





