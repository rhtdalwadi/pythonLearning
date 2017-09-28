from random import randint

min,max = 1,6


def drs():
    print randint(min,max)

choice = raw_input('Would you like to roll the dice? Y/N')

while (choice in ('Y','y')):
    drs()
    choice = raw_input('Would you like to roll the dice? Y/N')

print 'Thank you for rolling the dice.'