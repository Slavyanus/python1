
x = int (input ("Введите координату х: "))
y = int (input ("Введите координату y: "))

if x > 0 and y > 0:
    print ("Первая четверть")
elif x < 0 and y > 0:
    print ("Вторая четверть")
elif x < 0 and y < 0:
    print ("Третья четверть")
elif x > 0 and y < 0:
    print ("Четвертая четверть")
else:
    print ("Введите координаты больше нуля")