# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
days=['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
number = int(input("введите номер дня недели  ")) -1
if 0 <= number <=6:
    print((days[number]))
    if number > 4 :
        print("Выходной")
    else: 
     print("Будний день")    
else:
    print("Нет такого дня недели ")

