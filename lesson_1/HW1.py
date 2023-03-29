'''
Выполнение
задания
№ 1
'''
a = 1
b = 10
d = 15
print(a, b, d)

name = input()
print('Привет', name)


age = int(input())
print("Вам", age)

"""
Выполнение
задания 
№ 2
"""
sec = input()
if sec.isdigit() == 1:
    sec = int(sec)
    hour = sec // 3600
    sec = sec % 3600
    min = sec // 60
    sec = sec % 60

    print('Часы:', hour)
    print("Минуты:", min)
    print("Секунды", sec)
else:
    print('Вы ввели не число.')

"""
Выполнение
задания
№ 3
"""
n = int(input("Введите целое число от 1 до 9: "))

nn = n*10+n  # например нужно получить 88: 8*10+8
nnn = n*100+nn # или nn*10+n

sum = n + nn + nnn
print("Сумма", n, "+", nn, "+", nnn, "=", sum)



