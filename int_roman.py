
def int_to_roman(N):

    Unit = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    Dozens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    Hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    Thousands = ["", "M", "MM", "MMM"]

    u = N % 10
    d = int(N / 10) % 10
    h = int(N / 100) % 10
    t = int(N / 1000) % 10
    number = 0

    if (N >= 1000):
        number = (Thousands[t] + Hundreds[h] + Dozens[d] + Unit[u])
    elif (N >= 100):
        number = (Hundreds[h] + Dozens[d] + Unit[u])
    elif (N >= 10):
        number = (Dozens[d] + Unit[u])
    else:
        number = (Unit[N])
    return(number)


if __name__ == '__main__':
    N = int(input("Input integer number (between 1 and 3000: "))
    if (N == 0):
        print ("Please enter a number greater than 0")
    elif (N > 3000):
        print ("Please enter a number less than 3000")
    else:
            print "Roman number is:", int_to_roman(N)
    
