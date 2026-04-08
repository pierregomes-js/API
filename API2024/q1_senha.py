def main():
    digitos = int(input('Quantidade de digitos da senha: '))
    satisfeito = 'N'
    semente = 42


    while satisfeito == 'N':

        senha = gerador_senhas(digitos, semente)

        print(f'Senha: {senha}')
        satisfeito = input('Satisfeito? (S/N): ')
        semente = (semente * 997 + 12345) % 1000000



def gerador_senhas(digitos, semente):
    senha = ''
    n = 0
    ultimo_digito = 0
    base = semente

    while n <= digitos:
        base = (base * 1103515245 + 12345) % (2**31)
        digito = (base // 65536) % 10

        eh_igual = (ultimo_digito == digito)
        eh_ant = (ultimo_digito - 1 == digito)
        eh_suc = (ultimo_digito + 1 == digito)

        if not (eh_igual or eh_ant or eh_suc):
            senha = senha + str(digito)
            ultimo_digito = digito
            n += 1

    return senha
        
        

main()