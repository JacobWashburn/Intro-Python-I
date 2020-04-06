import math
import os

primes_list = []
number = ''
message = "\n-- Input a number to see if it's prime. \n" \
          "-- Decimal Numbers will be reduced to the nearest whole " \
          "number. \n" \
          "-- Type 1 to reset.\n" \
          "-- Type 0 to exit. \n"


def clear():
    # This os command works on my computer but requires giving the terminal security
    # access which is not acceptable in most cases. I just wanted the functionality
    # it gave. If it gives you trouble just comment out lines 18 & 19.

    os.system(
            "osascript -e 'tell application \"System Events\" to keystroke \"k\" using command down'")
    print(message)


def check_num(num):
    for i in range(2, num):
        if num % i == 0:
            return f'\n"{num}" is not a prime number.\n'
    else:
        if num not in primes_list:
            primes_list.append(num)
            return (f'\n"{num}" is a prime number.\n'
                    f'You discovered a new Prime number!\n')
        else:
            return f'\nYou already discovered the Prime number: "{num}".\n'


def confirm_reset():
    confirm = input('Are you sure you like to erase all discovered Primes and start over? Y or N: ').lower()
    while confirm not in ('y', 'n'):
        print('Please enter "Y" or "N".')
        confirm = input('Are you sure you like to erase all discovered Primes and start over? Y or N: ').lower()
    if confirm == 'y':
        primes_list.clear()
        clear()
    else:
        clear()


clear()

while number != 0:
    primes_list.sort()
    if len(primes_list):
        print('Primes you have discovered: ', primes_list)
    try:
        number = math.floor(float(input('Input a number:')))
    except:
        clear()
        print('\nPlease provide a valid number.\n')
        continue
    if number > 1:
        clear()
        print(check_num(number))
    elif number == 1:
        confirm_reset()
    else:
        clear()
        print('\n-----------------\n'
              '-----------------\n'
              '--- Good-Bye! ---\n'
              '-----------------\n'
              '-----------------\n')
