#%%

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# num_letter = ""
# for letra in range(0, nr_letters):
#     num_letter += random.choice(letters)
#
# num_simbol = ""
# for simbol in range(0, nr_symbols):
#     num_simbol += random.choice(symbols)
#
# num_numbers = ""
# for numeros in range(0, nr_numbers):
#     num_numbers += random.choice(numbers)
#
# pasword = num_letter + num_simbol + num_numbers
# pasword_list=list(pasword)
# random.shuffle(pasword_list)
# print(pasword_list)

# hard difficult
pasword_list=[]
for char in range(0,nr_letters):
    pasword_list.append(random.choice(letters))

for char in range(0,nr_numbers):
    pasword_list.append((random.choice(numbers)))

for char in range(0,nr_symbols):
    pasword_list.append(random.choice(symbols))

print(pasword_list)
random.shuffle(pasword_list)
print(pasword_list)

pasword=''

for char in pasword_list:
    pasword+=char

print(f"Your pasword is: {pasword} sigamos avanzando")
# %%
