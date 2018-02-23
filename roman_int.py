def roman_to_int(roman_number):
    result = 0

    values = {
        'M' : 1000,'D' : 500,'C' : 100,'L' : 50,'X' : 10,'V' : 5,'I' : 1
    }

    if len(roman_number) > 0:
        previous_value = roman_number[0]
    for letter in roman_number:
        if letter in values:
            actual_value = values[letter]
        
            if previous_value >= actual_value:
                result += actual_value
            else:
                result += actual_value - (2 * previous_value)
            previous_value = actual_value
        else:
            print 'Valor invalido:'
    return result

if __name__ == '__main__':
    roman_number = raw_input("Input roman number: ").upper()
    if not (roman_number is values):
        print(" Erro ")
    else: 
         print "Integer number is:", roman_to_int(roman_number)