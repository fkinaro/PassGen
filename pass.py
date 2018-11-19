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
pass_len = int(input('How long sholud the password be?\n'))

# main part of the program
if pass_len < 20:
    print('That is a short password.\nThe default is 20 characters long.')
    pass_len = 20
    rounds(pwds)
else:
    rounds(pwds)
