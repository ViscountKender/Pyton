# Сформировать список из  N членов последовательности.Для N = 5: 1, -3, 9, -27, 81 и т.д.
number = int(input("Введите число членов последовательности: "))
print("N =",number,": 1",end="")
i = 1
x = 1
while i < number :
    temp = x *(-3)
    x = temp
    if i < number :
        print(end=", ")
    print(x,end="")
    i = i + 1





