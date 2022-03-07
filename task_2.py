# Найти максимальное из пяти чисел
a = int(input("Введите число : "))
b = int(input("Введите число : "))
c = int(input("Введите число : "))
d = int(input("Введите число : "))
e = int(input("Введите число : "))
max_1 = a
if max_1 < b:
    max_1 = b
if max_1 < c:
    max_1 = c
if max_1 < d:
    max_1 = d
if max_1 < e:
    max_1 = e

print( max_1)


