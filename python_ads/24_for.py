# Task 1

import random

activities = ['swap', 'approve', 'lend', 'stake', 'mint']

symbol = 'abcdef0123456789'
wallets = []
counter = 0

# wallets = ["0x" + "".join(random.choices("abcdef0123456789", k=40)) for _ in range(100)]

while counter < 100:
    wallet = '0x'

    while len(wallet) < 40:
        wallet += random.choice(symbol)

    wallets.append(wallet)
    counter += 1

balances = [0] * 100
transactions = [0] * 100

while sum(transactions) < len(wallets) * 10:

    for index_wallet, wallet in enumerate(wallets):
        if transactions[index_wallet] >= 10:
            continue

        if balances[index_wallet] == 0:
            deposit = random.randint(1, 3)
            balances[index_wallet] += deposit
            print(f'Баланс кошелька - {wallet} - 0, Вывод с биржи - {deposit}, Баланс стал - {balances[index_wallet]}')

        activ = random.choice(activities)
        trans_cost = random.randint(1, 2)
        print(f'Для кошелька {wallet}, выбрана активность - {activ}, стоимость - {trans_cost}')

        if balances[index_wallet] < trans_cost:
            add_deposit = trans_cost - balances[index_wallet]
            balances[index_wallet] += add_deposit
            print(f'Для кошелька {wallet}, не хватает на активность, Вывод с биржи - {add_deposit}, Баланс стал - {balances[index_wallet]}')

        balances[index_wallet] -= trans_cost
        transactions[index_wallet] += 1
        print(f'Баланс кошелька {wallet}, после {transactions[index_wallet]} активностей стал - {balances[index_wallet]}')

print(f'Все {len(wallets)} кошельков, сделали по 10 транзакций')

# Task 2

import random

passwords_one = [("".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=4)) + "".join(random.choices("0123456789", k=4))) for _ in range(100)]
passwords_two = [password.upper() for password in passwords_one]
passwords_tree = [password for password in passwords_two if "D" in password]

print(passwords_one)
print(passwords_two)
print(passwords_tree)

