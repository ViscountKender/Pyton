# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
sec = int(input('Введите первое число: '))
day = sec // 86400
time = sec % 86400 // 3600
min = sec % 3600//60
sec1 = sec % 60


print("дней:",day, "часов:",time, "минут:",min,"секунд:",sec1)

 
# 100000 сек это 1 день, 3 часа 46 мин 4 сек