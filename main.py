from int_roman import *
from roman_int import *

def decision_method(number_choice):
    if (number_choice == 1):
        N = int(input("Input integer number (between 1 and 3000: "))
        if (N == 0):
            print ("Please enter a number greater than 0")
        elif (N > 3000):
            print ("Please enter a number less than 3000")
        else:
            print "Roman number is:", int_to_roman(N)
    elif (number_choice == 2):
        roman_number = raw_input("Input roman number: ").upper()
        print "Integer number is:", roman_to_int(roman_number)
        
    else: 
        print "--------- Input a valid Number ---------"

if __name__ == '__main__':
    print "Please choose a number"
    number_choice= int(input("1- Integer to Roman or 2- Roman to Integer: "))
    decision_method(number_choice)