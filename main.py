# Program to print out the alphabet
# Requested by: Fred Flintstone
# Author: DR7262
# Date written: 04/06/2024
# Date tested and approved: 2/1/2022
# Revision History:
# 2/1/2022 changed the name of the file variable

import sys

print("Password Checker V0.1")

user_pw = input("Please enter your password:")

# 10 - 25 is the current acceptable password length
if len(user_pw) not in range(10, 25):
    print("Password is not strong enough - please revise.")
    sys.exit()

symbols_allowed = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
    '_', '=', '+', '[', '{', ']', '}', '|', ';', ':', ',', '<', '.', '>', '?']

symbols_in_password = 0
for character in user_pw:
    if character in symbols_allowed:
        symbols_in_password += 1
# 2 is currently the minimum number of acceptable symbols required in the password
if symbols_in_password < 2:
    print("Password is not strong enough - please revise.")
    sys.exit()
    

numbers_in_password = 0
for character in user_pw:
    if character in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        numbers_in_password += 1
# 2 is currently the minimum number of digits required in the password
if numbers_in_password < 2:
    print("Password is not strong enough - please revise.")
    sys.exit()

uppercase_chars_in_password = 0
for character in user_pw:
    if character.isupper():
        uppercase_chars_in_password += 1
#2 is currently the minimum number of uppercase characters required in the password
if uppercase_chars_in_password < 2:
    print("Password is not strong enough - please revise.")
    sys.exit()

print("Password is strong enough.")