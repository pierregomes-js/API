def main():
    def receber_inteiro(texto):
        try:
            numero = int(input(texto))
        except:
            while True:
                print('Número inválido.')
                numero = int(input(texto))
        return numero
    
    def receber_inteiro_positivo(texto):
        numero = receber_inteiro(texto)
        if numero < 0:
            while numero < 0:
                print('Número inválido.')
                numero = receber_inteiro(texto)
        return numero

    n = receber_inteiro_positivo(': ')


main()