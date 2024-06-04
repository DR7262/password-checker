# Program to print out the alphabet
# Requested by: Fred Flintstone
# Author: DR7262
# Date written: 04/06/2024
# Date tested and approved: 2/1/2022
# Revision History:
# 2/1/2022 changed the name of the file variable

print("Password Checker V0.1")

user_pw = input("Please enter your password:")

flags = 0
if len(user_pw) not in range(10, 25):
    flags+=1

symbols_allowed = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
    '_', '=', '+', '[', '{', ']', '}', '|', ';', ':', ',', '<', '.', '>', '?']

symbols_in_password = 0
for character in user_pw:
    if character in symbols_allowed:
        symbols_in_password +=1

# As discussed, minimum number of acceptable symbols in password is 2
if symbols_in_password < 2:
    flags+=1

if flags == 0:
    print("Password is strong enough.")
else:
    print("Password is not strong enough - please revise.")