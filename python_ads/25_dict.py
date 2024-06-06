import random
import time

# Запрос количества кошельков
wallets_amount = int(input("Введите количество кошельков: "))
min_transactions = int(input("Введите минимальное количество транзакций: "))

gas = random.randint(10, 50)
gas_limit = 30

# Генерация стоимости активностей
activities_prices = {
    'swap': random.randint(10, 100),
    'mint_nft': random.randint(10, 100),
    'burn_nft': random.randint(10, 100),
}

# Генерация кошельков и их начального состояния
my_wallets = {}
for _ in range(wallets_amount):
    wallet_address = '0x' + ''.join([random.choice('abcdef0123456789') for _ in range(40)])
    eth_balance = random.uniform(0.2, 0.8)
    usdc_balance = random.randint(0, 50)
    my_wallets[wallet_address] = {
        'balances': {'ETH': eth_balance, 'USDC': usdc_balance},
        'transactions': 0,
        'activities': {'swap': 0, 'mint_nft': 0, 'burn_nft': 0}
    }

wallets_list = list(my_wallets.keys())

while wallets_list:
    # Изменяем газ в случайную сторону
    if gas <= 10:
        direction = 1
    elif gas >= 50:
        direction = -1
    else:
        direction = random.choice([-1, 1])

    gas += direction

    print(f"Газ: {gas}")
    time.sleep(0.1)

    # Проверка, достиг ли газ рабочего уровня
    if gas < gas_limit:
        print(f"Газ рабочий: {gas}")

        # Выбор случайного кошелька из списка активных кошельков
        wallet = random.choice(wallets_list)

        activities = my_wallets[wallet]['activities']

        # Логика выбора активности
        if all(activities.values()) or not any(activities.values()):
            random_activity = random.choice(list(activities.keys()))
        else:
            zero_activities = [activity for activity in activities if not activities[activity]]
            random_activity = random.choice(zero_activities)

        price_activity = activities_prices[random_activity] * gas / 10000  # стоимость активности в ETH

        if price_activity > my_wallets[wallet]["balances"]["ETH"]:  # если стоимость активности больше баланса ETH
            withdraw_amount = price_activity * 2 * random.uniform(1.1, 1.2)  # сумма вывода с биржи
            my_wallets[wallet]["balances"]["ETH"] += withdraw_amount  # добавление суммы вывода на баланс ETH
            print(
                f"Кошелек {wallet} вывел {withdraw_amount:.2f} ETH с биржи для выполнения транзакции {random_activity}")

        if random_activity == "swap":  # если активность swap
            eth_usdc_price = random.randint(2000, 3000)  # стоимость ETH в USDC
            if my_wallets[wallet]["balances"]["USDC"]:  # если баланс USDC не нулевой
                my_wallets[wallet]["balances"]["ETH"] += my_wallets[wallet]["balances"][
                                                             "USDC"] / eth_usdc_price  # обмен USDC на ETH
                my_wallets[wallet]["balances"]["USDC"] = 0  # обнуление баланса USDC
            else:
                swap_amount = random.uniform(0, my_wallets[wallet]["balances"]["ETH"] - price_activity)  # сумма обмена
                my_wallets[wallet]["balances"]["ETH"] -= swap_amount  # списываем сумму обмена
                my_wallets[wallet]["balances"]["USDC"] += swap_amount * eth_usdc_price  # добавляем сумму обмена в USDC

        my_wallets[wallet]["balances"]["ETH"] -= price_activity  # списываем стоимость активности с баланса ETH

        print(f"Кошелек {wallet} выполнил активность {random_activity} за {price_activity:.6f} ETH")
        my_wallets[wallet]["transactions"] += 1  # увеличиваем количество транзакций
        my_wallets[wallet]["activities"][random_activity] += 1  # увеличиваем количество транзакций по активности

        if my_wallets[wallet]["transactions"] >= min_transactions:  # если количество транзакций достигло минимального
            wallets_list.remove(wallet)  # удаляем кошелек из списка

        time.sleep(random.uniform(0.5, 1.5))  # пауза

for wallet, data in my_wallets.items():  # вывод результатов
    print(f"Кошелек {wallet}:")
    print(f"--- Баланс ETH: {data['balances']['ETH']:.6f}")
    print(f"--- Баланс USDC: {data['balances']['USDC']}")
    print(f"--- Количество транзакций: {data['transactions']}")
    print(f"--- Количество транзакций swap: {data['activities']['swap']}")
    print(f"--- Количество транзакций mint_nft: {data['activities']['mint_nft']}")
    print(f"--- Количество транзакций burn_nft: {data['activities']['burn_nft']}")