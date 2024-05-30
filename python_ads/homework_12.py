# Task 1
import random
import time

gen_wallets = int(input('Сколько кошельков сгенерировать: '))
drop_counter = int(input('Сколько дропов нужно раздать: '))

while True:
    if drop_counter > gen_wallets:
        print('Количество кошельков получивших дроп не должно быть больше уол-ва кошельков участников')
        print('Введите значения заново: ')
        gen_wallets = int(input('Сколько кошельков сгенерировать: '))
        drop_counter = int(input('Сколько дропов нужно раздать: '))
    else:
        break

symbol = 'abcdef0123456789'
wallets = []
drop_wall = []
counter = 0


while counter < gen_wallets:
    wallet = '0x'

    while len(wallet) < 40:
        wallet += random.choice(symbol)

    wallets.append(wallet)
    counter += 1

print(f'Всего в раздаче дропа участвует {gen_wallets} кошельков:')
print('\n'.join(wallets))

counter = 0
while counter < drop_counter:
    drop = wallets.pop(random.randint(0, len(wallets)-1))
    drop_wall.append(drop)
    counter += 1

print()
print(f'Из этого списка получили дроп {drop_counter} кошельков:')
print('\n'.join(drop_wall))

copy_drop_wall = drop_wall.copy()

print()
while len(drop_wall) > 0:
    pause = random.randint(2, 7)
    wall = drop_wall.pop(random.randint(0, len(drop_wall) - 1))
    print(f'Клейм токенов на кошельке: {wall}')
    print(f'Пауза {pause}')
    time.sleep(pause)

print()

dex_wallets = []
counter = 0

while counter < drop_counter:
    wallet = '0x'

    while len(wallet) < 40:
        wallet += random.choice(symbol)

    dex_wallets.append(wallet)
    counter += 1

print(f'Суб аккаунты с биржи:')
print('\n'.join(dex_wallets))

counter = 0

print()
print('Вывод на биржу:')
while counter < drop_counter:
    print(f"{copy_drop_wall[counter]} -> {dex_wallets[counter]}")
    pause = random.randint(2, 7)
    print(f'Пауза {pause}')
    time.sleep(pause)
    counter += 1

# Task 2

import random
import time

activities = ['swap', 'brige', 'mint', 'wrap', 'unwrap', 'lend', 'borrow', 'liquidity', 'deploy', 'checkin']
symbol = 'abcdef0123456789'
wallets = []
counter = 0

while counter < 10:
    wallet = '0x'

    while len(wallet) < 40:
        wallet += random.choice(symbol)

    wallets.append(wallet)
    counter += 1

while wallets:
    wallet = random.choice(wallets)
    wallets_activ = activities.copy()
    while wallets_activ:
        activ = random.choice(wallets_activ)
        print(f'Кошелек {wallet} делает {activ}')
        pause = random.randint(1, 2)
        print(f'Пауза {pause} сек')
        time.sleep(pause)
        print()
        wallets_activ.remove(activ)

    wallets.remove(wallet)

# Task 3

import random
import time

wallets = []
transactions = []

while len(wallets) < 10:
    wallet = "0x"  # начало кошелька

    while len(wallet) < 42:
        wallet += random.choice("abcdef0123456789")

    if wallet not in wallets:
        wallets.append(wallet)

while len(wallets) > len(transactions):
    count = random.randint(0, 3)
    transactions.append(count)

target_transactions = int(input('Какое мин. кол-во транз должно быть на коше:'))

index = 0
while index < len(wallets):
    print(f"Кошелек {wallets[index]} имеет {transactions[index]} транзакций")
    index += 1

work_wallets = wallets.copy()  # копируем список кошельков для работы

print("Начинаем работу\n")

while work_wallets:
    if random.randint(0,1):
        wallet = random.choice(work_wallets)
        wallet_index = wallets.index(wallet)
    else:
        min_trans = min(transactions)
        wallet_index = transactions.index(min_trans)
        wallet = wallets[wallet_index]

    if transactions[wallet_index] < target_transactions:
        work_transaction = random.randint(1, 5)
        transactions[wallet_index] += work_transaction
        print(f"Кошелек {wallet} выполнил транзакций - {work_transaction}, всего транзакций - {transactions[wallet_index]}")
        time.sleep(random.uniform(0.1, 0.3))

    if transactions[wallet_index] >= target_transactions:
        print(f"Кошелек {wallet} уже выполнил минимальное количество транзакций - {transactions[wallet_index]}")
        work_wallets.remove(wallet)

print('Работа завершена')






# print(wallets)
# print(len(wallets))
# print(trans)
# print(len(trans))
