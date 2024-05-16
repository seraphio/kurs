# Task 1

balance = int(input('Input wallet balance($): '))

if balance <= 0:
    print('нищий')
elif 1 <= balance <= 100:
    print('нормис')
elif 101 <= balance <= 1000:
    print('деген')
elif 1001 <= balance <= 10000:
    print('кит')
else:
    print('Илон Маск')


# Task 2
import random

gen_gas = random.randint(10, 100)
gen_balance = random.randint(2000, 10000)
brige_scroll = gen_gas * 75
swap_scroll = gen_gas * 40
clusters = gen_gas * 100
all_trans = brige_scroll + swap_scroll + clusters

print(f'Текущий газ: {gen_gas} Gwei')
print(f'Ваш баланс: {gen_balance}$')

if all_trans <= gen_balance:
    print(f'На балансе не достаточно средств, нужно вывести: {gen_balance - all_trans}$')
    withdrawal = gen_balance - all_trans
    gen_balance = gen_balance + withdrawal
    print(f'Баланс обновлен: {gen_balance}$')

if 0 < gen_gas < 15:
    print(f'Делаю Clusters, мост Scroll и свапы Scroll, остаток на балансе: {gen_balance - clusters - brige_scroll - swap_scroll}$')

elif 15 < gen_gas < 25:
    print(f'Делаю мост Scroll и свапы Scroll, остаток на балансе: {gen_balance - brige_scroll - swap_scroll}$')

elif 25 < gen_gas < 50:
    print(f'Делаю свапы Scroll, остаток на балансе: {gen_balance - swap_scroll}$')
else:
    print('Высокий газ, жду!')

print('Работа завершена')


# Task 3

import time
import random

balance_eth = 1.93
balance_usdc = 2000
eth = 'ETH'
usdc = 'USDC'
cost_eth = 3500

print(f'Баланс: {balance_eth} {eth}, {balance_usdc} {usdc}')

if balance_usdc == 0:
    print(f'Меняю {eth} на {usdc}')
    sum_eth = (balance_eth - (balance_eth * (5 / 100)))
    print(f'Сумма обмена: {float(sum_eth):.2f} {usdc}')
    balance_eth = balance_eth - sum_eth
    balance_usdc = sum_eth * cost_eth
    print(f'Баланс: {float(balance_eth):.2f} {eth}, {int(balance_usdc)} {usdc}')

else:
    for _ in range(4):
        print(f'Меняю {usdc} на {eth}')
        # случайный % от всей суммы на балансе
        randon_swap = random.randint(3, 15) / 100
        amount_swap = balance_usdc * randon_swap
        print(f'Сумма свапа: {int(amount_swap)} {usdc}')
        balance_usdc = balance_usdc - amount_swap
        balance_eth = balance_eth + amount_swap / cost_eth
        pause_time = int(random.uniform(1, 10))
        print(f"Пауза на {pause_time} секунд(ы)...")
        time.sleep(pause_time)
        print("Продолжение работы...")
        print(f'Баланс: {float(balance_eth):.2f} {eth}, {int(balance_usdc)} {usdc}')

print("Завершение работы.")


