# При заданном целом числе n посчитайте n + nn + nnn.
number = int(input("Введите число: "))
result = number + number**2 + number**3
print(result)
