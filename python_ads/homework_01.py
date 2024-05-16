# task 1
name = 'Maf'
accounts = int(1000)
drop_for_acc = int(1000)
lambo_price = int(300000)

print(f"Hello, Brayan, My name is {name}, I have {accounts} accs LayerZero")
print(f"I want airdrop {drop_for_acc}$ for every acc")
print(f"Give me my drop = {accounts * drop_for_acc}$")
print(f"I want to buy Lambo, lambo price {lambo_price}$")
print(f"I want to buy {(accounts * drop_for_acc) // lambo_price} Lambo")
print(f"I still have some left {(accounts * drop_for_acc) % lambo_price}$")

# task 2
surname = "Max"
name = "Zarev"
surname, name = name, surname
full_name = name + " " + surname

print(f"My name is {name}, my surname is {surname}")
print(f"My full name is {full_name}")

# task 3
total = 0
print(total + 10)
print(total + 20)
print(total + 30)
print(total + 40)

# task 4
nachinka = int(input("С чем будет шаурма?(Курица - 1,Говядина - 2, Овощи - 3): "))
if 1 <= nachinka <= 3:
    lavash = int(input("Какой брать лаваш?(Обычный - 1, С сыром - 2): "))
    if 1 <= lavash <= 2:
        if nachinka == 1 and lavash == 1:
            print('Шаурма с курицей в обычном лаваше: "Нежная курица с хрустящими овощами в тонком лаваше."')
        elif nachinka == 1 and lavash == 2:
            print('Шаурма с курицей в лаваше с сыром: "Курица и ароматный сыр в лаваше – для гурманов."')
        elif nachinka == 2 and lavash == 1:
            print('Шаурма с говядиной в обычном лаваше: "Сытная говядина с овощами в мягком лаваше."')
        elif nachinka == 2 and lavash == 2:
            print('Шаурма с говядиной в лаваше с сыром: "Говядина и расплавленный сыр – вкусное сочетание."')
        elif nachinka == 3 and lavash == 1:
            print('Овощная шаурма в обычном лаваше: "Легкость и свежесть овощей в вашем лаваше."')
        elif nachinka == 3 and lavash == 2:
            print('Овощная шаурма в лаваше с сыром: "Идеальный баланс овощей и сыра в лаваше."')
    else:
        print('При выборе лаваша нужно вводить только цифры от 1 до 2')

else:
    print('При выборе начинки нужно вводить только цифры от 1 до 3')



