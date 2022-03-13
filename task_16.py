# Найти расстояние между двумя точками пространства
x = int(input("Введите X : "))
y = int(input("Введите Y : "))
x1 = int(input("Введите X1 : "))
y1 = int(input("Введите Y1 : "))

dist = ((x1 - x)**2 + (y1 - y)**2)**(1/2)

print(round(dist,2))

