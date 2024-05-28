# Task 1
text = input('Введите свой текст: ').split(' ')
print(text[::-1])

# Task 2
import time
import random
import re

gas_price = 50

while True:
    wallets_amount = input("Введите число кошельков: ")

    if re.match(r'^\d+$', wallets_amount):  # Проверяем на положительное целое число
        wallets_amount = int(wallets_amount)

        while True:
            drops_amount = input("Введите число кошельков получивших дроп: ")

            if re.match(r'^\d+$', drops_amount):  # Проверяем на положительное целое число
                drops_amount = int(drops_amount)
                break
            else:
                print("Это не число")
        break
    else:
        print("Это не число")

wallet_number = 0
wallets_with_drop = []

# Раздаем дропы до тех пор, пока количество дропов больше 0
while drops_amount > 0:
    wallet_number += 1

    flip = random.randint(0, 1)
    if flip == 0:
        print(f"Кошелек номер: {wallet_number} получил дроп")
        wallets_with_drop.append(wallet_number)
        drops_amount -= 1  # Уменьшаем количество оставшихся дропов
        gas_price = random.randint(15, 50)
        while gas_price > 30:  # Теперь ждем, пока газ будет ниже 30
            print(f"Цена на газ {gas_price} выше порога 30")
            time.sleep(1)
            print("Подождем нормального газа...")
            gas_price = random.randint(15, 50)
        print(f"Дроп клеймится, газ {gas_price}")
    else:
        print(f"Кошелек номер: {wallet_number} не получил дроп")

wallets_with_drop_str = ", ".join(map(str, wallets_with_drop))
print(f"Кошельки с дропом: {wallets_with_drop_str}")

# Task 3
min_num = int(input('Введите первое число списка: '))
max_num = int(input('Введите второе число списка: '))

base_list = list(range(min_num, max_num + 1))
print(f'Базовый список: {base_list}')

chet_list = []
counter = min_num - 1

while counter < max_num:
    counter += 1
    if counter % 2 == 0:
        chet_list.append(counter)

print(f'Четный список: {chet_list}')

counter = 0

while counter < len(chet_list):
    chet_list[counter] = chet_list[counter] ** 2
    counter += 1

print(f'Квадратный список: {chet_list}')

# Task 4

import random

while True:
    length_min = input("Введите минимальную длину пароля: ")
    if length_min.isdigit():
        length_min = int(length_min)
        break
    else:
        print("Ошибка, введите число")

while True:
    length_max = input("Введите максимальную длину пароля: ")
    if length_max.isdigit():
        length_max = int(length_max)
        if length_max >= length_min:
            break
        else:
            print(f"Ошибка, введите число больше или равное {length_min}")
    else:
        print("Ошибка, введите число")

passwords_amount = 0
while True:
    passwords_amount_input = input("Введите количество паролей: ")
    if passwords_amount_input.isdigit():
        passwords_amount = int(passwords_amount_input)
        break
    else:
        print("Ошибка, введите число")

symbols = "!@#$%^&*()_+{}[]"
digits = "0123456789"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()

password_characters = ""

symbols_input = input("Включать ли символы? (да/нет): ").strip().lower()
digits_input = input("Включать ли цифры? (да/нет): ").strip().lower()
uppercase_input = input("Включать ли заглавные буквы? (да/нет): ").strip().lower()
lowercase_input = input("Включать ли строчные буквы? (да/нет): ").strip().lower()

if symbols_input == "да":
    password_characters += symbols
if digits_input == "да":
    password_characters += digits
if uppercase_input == "да":
    password_characters += uppercase
if lowercase_input == "да":
    password_characters += lowercase

if password_characters == "":
    print("Вы не выбрали ни одного из вариантов, генерация символов будет произвольная")
    while password_characters == "":
        if random.choice([True, False]):
            password_characters += symbols
        if random.choice([True, False]):
            password_characters += digits
        if random.choice([True, False]):
            password_characters += uppercase
        if random.choice([True, False]):
            password_characters += lowercase

passwords = []

while passwords_amount > 0:
    password = ""
    password_length = random.randint(length_min, length_max)
    while len(password) < password_length:
        password += random.choice(password_characters)
    passwords.append(password)
    passwords_amount -= 1

print('\n'.join(passwords))

# Task 5

import random
import time

gas = random.randint(1, 100)
gas_list = []
counter = 0
pause_all = 0

while counter < 22:
    counter += 1
    pause = 1
    gas_list.append(gas)
    if random.randint(0, 1):
        gas += 1
    else:
        gas -= 1
    print(f'{gas} Gwei')
    time.sleep(pause)
    pause_all += pause

print(f'Газ который был за {pause_all} сек: {gas_list}')
print(f'Средний газ: {sum(gas_list) / len(gas_list):.2f} Gwei')

# Task 6
import random
import time

activ_list = ['swap', 'mint', 'stake', 'unstake', 'chekin', 'wrap', 'unwrap', 'liquid', 'deploy', 'brige']
trans_amount = int(input('Сколько транзакций нужно сделать:'))
all_time = 0
all_trans = trans_amount

while trans_amount > 0:
    random_pause = random.randint(2, 5)
    random_activ = random.choice(activ_list)
    time.sleep(random_pause)
    print(f'Делает {random_activ}')
    print(f'Пауза {random_pause}')
    all_time += random_pause + 1
    trans_amount -= 1

print(f'Сделал {all_trans} транзакций за {all_time} секунд')
