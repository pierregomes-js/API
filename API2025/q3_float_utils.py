def main():
    def receber_decimal(texto):
        try:
            numero = float(input(texto))
        except:
            while True:
                print('Número inválido, digite outro número.')
                numero = float(input(texto))
        return numero
    
    def receber_decimal_positivo(texto):
        numero = receber_decimal(texto)
        if numero < 0:
            while numero < 0:
                print('Número inválido.')
                numero = receber_inteiro(texto)
        return numero
    
    def receber_decimal_min(texto):
        numero = receber_decimal(texto)
        return numero

    def receber_decimal_max(texto):
        numero = receber_decimal(texto)
        return numero
    
    
    def receber_intervalo(texto, texto1, texto2):
        minimo = receber_decimal_min(texto1)
        maximo = receber_decimal_max(texto2)

        numero = receber_decimal(texto)
        if numero < minimo or numero > maximo:
            print('Número inválido.')
            numero = receber_decimal(texto)
        return

main()