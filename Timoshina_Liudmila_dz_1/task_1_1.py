second = int(input("Введите промежуток времени в секундах: "))
second = second % (24 * 3600)
hour = second // 3600
second %= 3600
minute = second // 60
second %= 60
print(hour, 'час', minute, 'мин', second, 'сек')