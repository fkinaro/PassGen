#!/usr/bin/env python3
import random


password = ''
chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()_-+=\|]}[{';:/?.>,<"

def passGen(pass_len):
    for c in range(pass_len):
        password = ''
        password += random.choice(chars)
        passw = str(password)
        print(passw, end='')


# used to call the password generator
# for a specified number of iterations
def rounds(pwds):
    while pwds > 0:
        passGen(pass_len)
        print('\n')
        pwds -= 1

pwds = int(input('How many passwords do you want?\n'))
pass_len = int(input('How long should the password be?\n'))

# main part of the program
if pass_len < 20:
    print('That is a short password.')
    print('Generating a random password...') # generate a password of 20 to 40 chars
    pass_len = int(random.choice(range(19, 71)))
    print(f'Generating a password of {pass_len} characters')
    rounds(pwds)
elif pass_len > 70:
    pass_len = int(random.choice(range(19, 71)))
    print(f'Too long\nGenerating a shorter password...\nPassword length: {pass_len}')
    rounds(pwds)
else:
    rounds(pwds)
