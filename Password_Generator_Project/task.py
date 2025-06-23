letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
import random
#easy level
r_letters=[]
for rl in range(0,nr_letters):
    r_letters.append(random.choice(letters))
#print(r_letters)

r_sym=[]
for rs in range(0,nr_symbols):
    r_sym.append(random.choice(symbols))
#print(r_sym)

r_num=[]
for rn in range(0,nr_numbers):
    r_num.append(random.choice(numbers))
#print(r_num)

password = ""
for pw in r_letters:
    password += pw
for pw in r_sym:
    password += pw
for pw in r_num:
    password += pw
print(f"Weak Password: {password}")

# hard level
new_list = r_letters + r_sym + r_num
#print(new_list)
random.shuffle(new_list)
new_password = ""
for new_pw in new_list:
    new_password += new_pw
print(f"Strong Password: {new_password}")
