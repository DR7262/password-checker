# Program to print out the alphabet
# Requested by: Fred Flintstone
# Author: DR7262
# Date written: 04/06/2024
# Date tested and approved: 2/1/2022
# Revision History:
# 2/1/2022 changed the name of the file variable

print("Password Checker V0.1")

user_pw = input("Please enter your password:")

if len(user_pw) in range(10, 25):
    print("Password is strong enough.")
else:
    print("Password is not strong enough - please revise.")
