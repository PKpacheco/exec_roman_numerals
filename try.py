#!/usr/bin/python


def roma_to_int(num):
    roma = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    romano = num[0].upper()
    letras = list(romano)
    resultado = 0
    anterior = 0
    for letra in letras:
        if letra in roma:
            if roma[letra] > anterior:
                resultado = resultado - anterior * 2
                resultado = resultado + roma[letra]
            else:
                resultado = resultado + roma[letra]
            anterior = roma[letra]
        else:
            print 'Letras desconocidas'
    print resultado


if __name__ == '__main__':
    num = raw_input(str("Entre com numero romano: "))
    roma_to_int(num)
