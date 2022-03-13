# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти
number = int(input('Введите число: '))
if 1 < number > 4:
    print("Неверный ввод")
if number == 1:
        print("x > 0 & y > 0 ")   
if number == 2:
         print("x < 0 & y > 0 ")   
if number == 3:
    print("x < 0 & y < 0 ")     
if number == 4:
    print("x > 0 & y < 0 ")


