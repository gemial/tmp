__author__ = 'student'
print('Hello World')
c = 10
print(c)

S = str(input())
print(S.replace('','*')[1:-1])

начальное_значение = 1
конечное_значение = 10

i = начальное_значение
while i < конечное_значение:
    print(i,i*2,sep=',')
    i += 1

print(1, 2, 3)
print(1, 2, 3, sep='')
print(1, 2, 3, sep='~')