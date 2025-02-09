from re import fullmatch
from math import ceil


def sprint(*args):  # simple with separator and end is nothing
    print(*args, sep='', end='')


def is_correct_number(number):  # check number to fraction
    if fullmatch(r'-?\d+/?-?\d+', number):
        num1, num2 = map(lambda x: abs(int(x)), number.split('/'))
        if num2 == 0:
            raise ZeroDivisionError('Division by zero')
        return num1, num2
    elif fullmatch(r'-?\d+', number):
        return abs(int(number)), 1
    else:
        raise ValueError('Wrong number')


def do_fraction_is_correct(num):  # do from incorrect fraction to correct fraction
    num = num.lower().replace(':', '/').replace('\\', '/')
    num1, num2 = is_correct_number(num)

    sign = '-' if num.count('-') % 2 == 1 else ''
    fraction_is_correct = False

    sprint(num)
    while not fraction_is_correct:
        for i in range(2, ceil(min(num1, num2)**0.5) + 1):
            if num1 % i == 0 and num2 % i == 0:
                num1 //= i; num2 //= i
                sprint(' = ', sign, num1, '/', num2)
                break
        else:
            fraction_is_correct = True

    if num1 >= num2 or num1 == 0:
        sprint(' = ')
        if num1 % num2 == 0:
            sprint(num1 // num2)
        else:
            sprint(num1 // num2, ' ', num1 % num2, '/', num2)

    print()

