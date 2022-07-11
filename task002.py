# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multiplication_list(number):
    # mult = 1
    mult_list = [1]
    while True:
        try:
            number = int(number)
            if number > 0:
                break
            else:
                print(f'Вы ввели число меньше 1')
                number = input('Введите число N: ')
        except ValueError:
            print(f'Вы ввели не число')
            number = input('Введите число N: ')
    for i in range(1, number):
        # mult *= i
        mult_list.append(mult_list[i-1] * (i+1))
        # mult_list.append(mult)
    return mult_list


N = input('Введите число N: ')
print(f'Набор произведений чисел от 1 до N: {multiplication_list(N)}')
