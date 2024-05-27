# Task 1
import random

print(f'Угадайка загадала число от 1 до 50, у вас 5 попыток')

while True:
    x = int(random.randint(1, 50))
    count = 0

    while count < 5:
        y = int(input("Введите число: "))
        count += 1
        print(x)
        if x == y:
            print(f'Поздравляю, вы угадали загаданное число, за {count} попытки(ок)')
            break
        elif x > y:
            print(f'Загаданное число больше {y}, у вас еще {5 - count} попытка(и)')
        else:
            print(f'Загаданное число меньше {y}, у вас еще {5 - count} попытка(и)')

    print(f"Игра окончена, загаданное число было - {x}")

    play_again = input("Хотите сыграть еще раз? (да/нет): ")
    if play_again.lower() != "да":
        break

print("Спасибо за игру!")


# Task 2

import re

while True:
    num = input("Введите число: ")

    if re.match(r'^-?\d+(?:\.\d+)?$', num):
        num = int(num)
        break
    else:
        print("Это не число")

print(num)
while num > 0:
    if num == 1:
        break
    else:
        num -= 1
        print(num)

# Task 3
import time
import random
import re

gas_price = 50

while True:
    wallets_amount = input("Введите число кошельков: ")

    if re.match(r'^-?\d+(?:\.\d+)?$', wallets_amount):
        wallets_amount = int(wallets_amount)

        while True:
            drops_amount = input("Введите число кошельков получивших дроп: ")

            if re.match(r'^-?\d+(?:\.\d+)?$', drops_amount):
                drops_amount = int(drops_amount)
                break
            else:
                print("Это не число")

        break
    else:
        print("Это не число")

wallet_number = 0
wallets_with_drop = ''

while wallet_number < wallets_amount:
    wallet_number += 1
    flip = random.randint(0, 1)
    if flip == 0 and drops_amount > 0:
        print(f"Кошелек номер: {wallet_number} получил дроп")
        wallets_with_drop += f"{wallet_number}, "
        gas_price = random.randint(15, 50)
        while gas_price > 20:
            print(f"Цена на газ {gas_price} выше порога 20")
            time.sleep(1)
            print(f"Подождем нормального газа")
            gas_price = random.randint(15, 50)
        print(f"Дроп клеймится, газ {gas_price}")
        drops_amount -= 1
        gas_price = 50

    else:
        print(f"Кошелек номер: {wallet_number} не получил дроп")

# if drops_amount != 0 and wallet_number == wallets_amount:
#     wallet_number = 0


print(f"Кошельки с дропом: {wallets_with_drop}")


