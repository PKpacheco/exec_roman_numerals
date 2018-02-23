def roman_to_int(numero_romano):
    resultado = 0

    valores = {
        'M' : 1000,
        'D' : 500,
        'C' : 100,
        'L' : 50,
        'X' : 10,
        'V' : 5,
        'I' : 1
    }

    if len(numero_romano) > 0:
        valor_anterior = numero_romano[0]
    for letra in numero_romano:
        if letra in valores:
            valor_atual = valores[letra]
        
            if valor_anterior >= valor_atual:
                resultado += valor_atual
            else:
                resultado += valor_atual - (2 * valor_anterior)
            valor_anterior = valor_atual
        else:
            print 'Valor invalido:'
    return resultado
numero_romano = raw_input("Numero Romano: ").upper()
print "Numero Inteiro:", roman_to_int(numero_romano)