import random

letters = ['a','b', 'C', 'd', 'e', 'f', 'G', 'h', 'I', 'j', 'K', 'l', 'M', 'n', 'o', 'p', 'q', 'R', 's', 'T', 'u', 'V', 'w', 'x', 'Y', 'z' ]
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!' , '#' , '$' , '%' , '&' , '(' , ')' , ':', '<']
print("Welcome to your password generator")
password = ""
n_letters = int(input("How many letters do you want in your password?\n"))
n_numbers = int(input("How many numbers do you want in your password?\n"))
n_symbols = int(input("How many symbols do you want in your password?\n"))

password_list = []
for i in range(1,n_letters+1):
    char = random.choice(letters)
    password_list += char

for i in range(1,n_numbers+1):
    char = random.choice(numbers)
    password_list += char
for i in range(1,n_symbols+1):
    char = random.choice(symbols)
    password_list += char
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(password)