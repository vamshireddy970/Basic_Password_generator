import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("Welcome to the Password Generator! ")
n_letters = int(input("Enter the number of letters you want to include: "))
n_symbols = int(input("Enter the number of symbols you want to include: "))
n_numbers = int(input("Enter the number of numbers you want to include: "))
Password_list = []
for i in range(1, n_letters+1):
    char = random.choice(letters)
    Password_list += char
for i in range(1, n_symbols+1):
    char = random.choice(symbols)
    Password_list += char
for i in range(1, n_numbers+1):
    char = random.choice(numbers)
    Password_list += char
random.shuffle(Password_list)
print(Password_list)
password = ""
for i in Password_list:
    password += i
print(password)