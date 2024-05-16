# Task 1
import random

min_int = int(input('Введите минимальную сумму: '))
max_int = int(input('Введите максимальную сумму: '))

random_amount = random.randint(min_int, max_int)

print(f'Вывод {random_amount} токенов с биржи на кошелек')

# Task 2
number = -15
# в степике были такие задачки
print(abs(number) + 10)

# Task 3
num = int(input('Введи любое число: '))

if num == 0:
    print('На "0" делить нельзя')
else:
    if num % 2 == 0:
        print('Число четное')
    else:
        print('Число нечетное')

# Task 4
balance = int(input('Введите баланс кошелька: '))
trans = int(input('Введите количество транзакций: '))
volume = int(input('Введите общий объем транзакций: '))
average_volume = int(volume / trans)

drop_min_balance = 500
drop_min_trans = 20
drop_volume = 5000
drop_average_volume = int(drop_volume / drop_min_trans)

if balance >= drop_min_balance and trans >= drop_min_trans and volume >= drop_volume and average_volume >= drop_average_volume:
    print('You are eligible')
else:
    print('You are NOT eligible')
