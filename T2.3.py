x = int(input('vvedite trehznachnoye chislo  '))
x1 = x//100
x2 = x//10-(x//100)*10
x3 = x%10
print('summa cifr = ', x1+x2+x3)