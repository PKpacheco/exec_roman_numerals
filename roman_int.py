import logging

VALUES = {
    'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
}


class RomanLetterInvalid(Exception):
    pass


def get_roman_letter():
    return str(input("Input roman letter: "))


def letter_validation(roman_letter):
    roman_letter = roman_letter.upper()
    if (roman_letter not in VALUES):
        raise RomanLetterInvalid("Please enter a valid roman letter")


def roman_to_int(roman_letter):
    result = 0
    if len(roman_letter) > 0:
        previous_value = roman_letter[0]
    for letter in roman_letter:
        if letter in VALUES:
            actual_value = VALUES[letter]
        if str(previous_value) >= str(actual_value):
            result += actual_value
        else:
            result += actual_value - (2 * previous_value)
        previous_value = actual_value
    return result


if __name__ == '__main__':
    try:
        roman_letter = get_roman_letter()
        letter_validation(roman_letter)
        print("Integer number is:", roman_to_int(roman_letter))
    except (Exception) as exp:
        logging.error(exp)
