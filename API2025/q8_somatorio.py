def main():
    numero = int(input('Digite um número: '))

    def eh_perfeito(numero):
        contador = 1
        somatorio_divisores = 0

        while contador < numero:
            if numero % contador == 0:
                somatorio_divisores += contador
            contador += 1

        if somatorio_divisores == numero:
            return True
        else:
            return False
        
    if eh_perfeito(numero):
        print(f'O número {numero} é perfeito.')
    else:
        print(f'O número {numero} não é perfeito.')



main()