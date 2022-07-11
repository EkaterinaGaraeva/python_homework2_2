# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

def sum_of_numbers():
    number = input('Введите вещественное число: ')
    sum = 0
    while True:
        try:
            float(number)
            break
        except ValueError:
            print(f'Вы ввели не число')
            number = input('Введите вещественное число: ')
    for i in number:
        if i not in '-.':
            sum += int(i)
    return (sum, number)


sum, n = sum_of_numbers()
print(f'Сумма цифр числа {n} равна {sum}')
