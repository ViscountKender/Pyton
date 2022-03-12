# При заданном целом числе n посчитайте n + nn + nnn.
number = (input("Введите число: "))
num1 = number + number
num2 = number + number + number
sum = int(number)+int(num1) + int(num2)
print(sum)

