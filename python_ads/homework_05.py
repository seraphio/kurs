# Taks 1

wallet = input('Введите кошелек: ')
url = 'https://debank.com/profile/'

print(url + wallet)

# Task 2(1)
import random

alf = 'abcdefghijklmnopqrstuvwxyz'
symbol1 = int(len(alf))
symbol2 = int(len('@#$%^&*'))

s1 = str(alf[random.randint(0, symbol1)]).lower()
s2 = str(alf[random.randint(0, symbol1)]).upper()
s3 = str(random.randint(0, 9))
s4 = ('@#$%^&*'[random.randint(0, symbol2)])

print(s1 + s2 + s3 + s4)

# Task 2(2)
import random
from random import choice

s1 = chr(random.randint(ord('a'), ord('z'))).lower()
s2 = chr(random.randint(ord('a'), ord('z'))).upper()
s3 = str(random.randint(0, 9))
s4 = choice('@#$%^&*')

print(s1 + s2 + s3 + s4)

# Task 3

password = input('Введите пароль: ')
symbol = len(password)

if symbol >= 8:
    print(True)
else:
    print(False)

# Task 4

text = input('Введите Имя, Фамилию, Возраст: ').strip()

name, lastname, age = text.split()
text_out = f"{(name +' ') * 3}{(lastname + ' ') * 4}{int(age) + 10}"

print(text_out)

# Task 5

x = 11

print((" " * 5 + "*" * 1).center(x))
print((" " * 4 + "*" * 3).center(x))
print((" " * 3 + "*" * 5).center(x))
print((" " * 2 + "*" * 7).center(x))
print((" " * 1 + "*" * 9).center(x))
print(("*" * 11).center(x))
print((" " * 5 + "*" * 1).center(x))
print((" " * 4 + "*" * 3).center(x))

# Task 5.1

text = input('Введите текст: ').strip()

text2 = text[::-1]

print(text2)

# Task 6

password = input('Введите пароль: ')

true_password = 'password123'

if password == true_password:
    print(True)
else:
    print(False)







