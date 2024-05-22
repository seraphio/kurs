# Task 1

x = int(input('Введите число: '))

if x > 0 and x % 2 == 0:
    print('Число положительное и четное')
elif x < 0 and x % 2 == 0:
    print('Число отрицательное и четное')
elif x < 0 and x % 2 != 0:
    print('Число отрицательное и нечетное')
elif x > 0 and x % 2 != 0:
    print('Число положительное и нечетное')

Task 2
import random

num = int(input('Введите кол-во символов от 5 до 8 для генерации пароля: '))

if not 5 <= num <= 8:
    num = random.randint(5, 8)
    print(f'Автоматическая генерация кол-ва символов пароля = {num}')

small = 'abcdefghijklmnopqrstuvwxyz'
big = small.upper()
digits = '0123456789'
special = '!@#$%^&*()-_+='

include_small = input('Включать ли в пароль строчные буквы (0 - да/1 - нет)?: ')
include_big = input('Включать ли в пароль прописные буквы (0 - да/1 - нет)?: ')
include_digits = input('Включать ли в пароль цифры (0 - да/1 - нет)?: ')
include_special = input('Включать ли в пароль спецсимволы (0 - да/1 - нет)?: ')

if include_small == '1' and include_big == '1' and include_digits == '1' and include_special == '1':
    print("Вы не выбрали ни одного диапазона символов для пароля.")

password = ''

if include_small == '0':
    password = password + random.choice(small)
if include_big == '0':
    password = password + random.choice(big)
if include_digits == '0':
    password = password + random.choice(digits)
if include_special == '0':
    password = password + random.choice(special)

if include_small == '0':
    password = password + random.choice(small)
if len(password) < num:
    if include_big == '0':
        password = password + random.choice(big)
    if include_digits == '0' and len(password) < num:  # проверка на длину пароля до конца программы
        password = password + random.choice(digits)
    if include_special == '0' and len(password) < num:
        password = password + random.choice(special)

    if len(password) < num:
        if include_small == '0':
            password = password + random.choice(small)
        if include_big == '0':
            password = password + random.choice(big)
        if include_digits == '0' and len(password) < num:  # проверка на длину пароля до конца программы
            password = password + random.choice(digits)
        if include_special == '0' and len(password) < num:
            password = password + random.choice(special)

        if len(password) < num:
            if include_small == '0':
                password = password + random.choice(small)
            if include_big == '0':
                password = password + random.choice(big)
            if include_digits == '0' and len(password) < num:  # проверка на длину пароля до конца программы
                password = password + random.choice(digits)
            if include_special == '0' and len(password) < num:
                password = password + random.choice(special)

            if len(password) < num:
                if include_small == '0':
                    password = password + random.choice(small)
                if include_big == '0':
                    password = password + random.choice(big)
                if include_digits == '0' and len(password) < num:  # проверка на длину пароля до конца программы
                    password = password + random.choice(digits)
                if include_special == '0' and len(password) < num:
                    password = password + random.choice(special)

                if len(password) < num:
                    if include_small == '0':
                        password = password + random.choice(small)
                    if include_big == '0':
                        password = password + random.choice(big)
                    if include_digits == '0' and len(password) < num:  # проверка на длину пароля до конца программы
                        password = password + random.choice(digits)
                    if include_special == '0' and len(password) < num:
                        password = password + random.choice(special)

                    if len(password) < num:
                        if include_small == '0':
                            password = password + random.choice(small)
                        if include_big == '0':
                            password = password + random.choice(big)
                        if include_digits == '0' and len(password) < num:  # проверка на длину пароля до конца программы
                            password = password + random.choice(digits)
                        if include_special == '0' and len(password) < num:
                            password = password + random.choice(special)

                        if len(password) < num:
                            if include_small == '0':
                                password = password + random.choice(small)
                            if include_big == '0':
                                password = password + random.choice(big)
                            if include_digits == '0' and len(
                                    password) < num:  # проверка на длину пароля до конца программы
                                password = password + random.choice(digits)
                            if include_special == '0' and len(password) < num:
                                password = password + random.choice(special)



print(password)

# Task 3
import random

gas_price = random.randint(15, 24)
balance = random.randint(0, 3)
tx_counter = random.randint(0, 3)
tx_target = 5

activity = 'Bridge' if gas_price < 20 else 'Swap'

if not balance == '0':
    withdraw = random.randint(1, 2)
    balance += withdraw
    print(f'Баланс нулевой, выведено {withdraw} и добавлено к балансу')
    print(f'Баланс: {balance}')

if activity == 'Bridge':
    if balance < 2:
        withdraw = 2 - balance
        print(f'Баланса не хватило на {activity}, вывел: {withdraw}')
        balance += withdraw

    balance -= 2
    print(f'{activity} стоит 2, сделана транзакция, балансе: {balance}')
    tx_counter += 1
    print(f'Транзакций в кошельке: {tx_counter}, осталось сделать: {tx_target - tx_counter}')
else:
    balance -= 1
    print(f'{activity} стоит 1, сделана транзакция, балансе: {balance}')
    tx_counter += 1
    print(f'Транзакций в кошельке: {tx_counter}, осталось сделать: {tx_target - tx_counter}')

# 2ой раз
if tx_counter < tx_target:
    if not balance == '0':
        withdraw = random.randint(1, 2)
        balance += withdraw
        print(f'Баланс нулевой, выведено {withdraw} и добавлено к балансу')
        print(f'Баланс: {balance}')

    gas_price = random.randint(15, 24)
    activity = 'Bridge' if gas_price < 20 else 'Swap'

    if activity == 'Bridge':
        if balance < 2:
            withdraw = 2 - balance
            print(f'Баланса не хватило на {activity}, вывел: {withdraw}')
            balance += withdraw

        balance -= 2
        print(f'{activity} стоит 2, сделана транзакция, балансе: {balance}')
        tx_counter += 1
        print(f'Транзакций в кошельке: {tx_counter}, осталось сделать: {tx_target - tx_counter}')

    else:
        balance -= 1
        print(f'{activity} стоит 1, сделана транзакция, балансе: {balance}')
        tx_counter += 1
        print(f'Транзакций в кошельке: {tx_counter}, осталось сделать: {tx_target - tx_counter}')

    # 3й раз
    if tx_counter < tx_target:
        if not balance == '0':
            withdraw = random.randint(1, 2)
            balance += withdraw
            print(f'Баланс нулевой, выведено {withdraw} и добавлено к балансу')
            print(f'Баланс: {balance}')

        gas_price = random.randint(15, 24)
        activity = 'Bridge' if gas_price < 20 else 'Swap'

        if activity == 'Bridge':
            if balance < 2:
                withdraw = 2 - balance
                print(f'Баланса не хватило на {activity}, вывел: {withdraw}')
                balance += withdraw

            balance -= 2
            print(f'{activity} стоит 2, сделана транзакция, балансе: {balance}')
            tx_counter += 1
            print(f'Транзакций в кошельке: {tx_counter}, осталось сделать: {tx_target - tx_counter}')

        else:
            balance -= 1
            print(f'{activity} стоит 1, сделана транзакция, балансе: {balance}')
            tx_counter += 1
            print(f'Транзакций в кошельке: {tx_counter}, осталось сделать: {tx_target - tx_counter}')

    # 4й раз
    if tx_counter < tx_target:
        if not balance == '0':
            withdraw = random.randint(1, 2)
            balance += withdraw
            print(f'Баланс нулевой, выведено {withdraw} и добавлено к балансу')
            print(f'Баланс: {balance}')

        gas_price = random.randint(15, 24)
        activity = 'Bridge' if gas_price < 20 else 'Swap'

        if activity == 'Bridge':
            if balance < 2:
                withdraw = 2 - balance
                print(f'Баланса не хватило на {activity}, вывел: {withdraw}')
                balance += withdraw

            balance -= 2
            print(f'{activity} стоит 2, сделана транзакция, балансе: {balance}')
            tx_counter += 1
            print(f'Транзакций в кошельке: {tx_counter}, осталось сделать: {tx_target - tx_counter}')

        else:
            balance -= 1
            print(f'{activity} стоит 1, сделана транзакция, балансе: {balance}')
            tx_counter += 1
            print(f'Транзакций в кошельке: {tx_counter}, осталось сделать: {tx_target - tx_counter}')

    # 5 раз
    if tx_counter < tx_target:
        if not balance == '0':
            withdraw = random.randint(1, 2)
            balance += withdraw
            print(f'Баланс нулевой, выведено {withdraw} и добавлено к балансу')
            print(f'Баланс: {balance}')

        gas_price = random.randint(15, 24)
        activity = 'Bridge' if gas_price < 20 else 'Swap'

        if activity == 'Bridge':
            if balance < 2:
                withdraw = 2 - balance
                print(f'Баланса не хватило на {activity}, вывел: {withdraw}')
                balance += withdraw

            balance -= 2
            print(f'{activity} стоит 2, сделана транзакция, балансе: {balance}')
            tx_counter += 1
            print(f'Транзакций в кошельке: {tx_counter}, осталось сделать: {tx_target - tx_counter}')

        else:
            balance -= 1
            print(f'{activity} стоит 1, сделана транзакция, балансе: {balance}')
            tx_counter += 1
            print(f'Транзакций в кошельке: {tx_counter}, осталось сделать: {tx_target - tx_counter}')




