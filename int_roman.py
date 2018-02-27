import logging

UNIT = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
DOZENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
THOUSANDS = ["", "M", "MM", "MMM"]


class RomanInvalidRange(Exception):
    pass


def get_num():
    return int(input("Input integer number (between 1 and 3000): "))


def value_validation(num):
    if (num < 0 or num > 3000):
        raise RomanInvalidRange("Please enter a number between 0 and 3000")


def int_to_roman(num):
    u = num % 10
    d = int(num / 10) % 10
    h = int(num / 100) % 10
    t = int(num / 1000) % 10
    number = 0

    if (num >= 1000):
        number = (THOUSANDS[t] + HUNDREDS[h] + DOZENS[d] + UNIT[u])
    elif (num >= 100):
        number = (HUNDREDS[h] + DOZENS[d] + UNIT[u])
    elif (num >= 10):
        number = (DOZENS[d] + UNIT[u])
    else:
        number = (UNIT[num])
    return number


if __name__ == '__main__':
    try:
        num = get_num()
        value_validation(num)
        print("Roman is :", int_to_roman(num))
    except (ValueError, RomanInvalidRange) as exp:
        logging.error(exp)
    except Exception as exp:
        logging.error(exp)
