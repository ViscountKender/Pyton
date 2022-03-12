# Сложите цифры целого числа.
number = int(input("Введите целое число: "))
sum = 0
while (number != 0):
    sum = sum + number % 10
    number = number //10
print("Сумма числа равна: ", sum)
