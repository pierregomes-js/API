def main():
    nome = input('Nome: ')
    T = len(nome)
    if T % 2 == 0:
        print(f'Os próximos {T} múltiplos de {T}: ')
        for i in range(2, T+2):
            print(T * i)
    else:
        print(f'Divisores de {T}: ')
        for i in range(1, T+1):
            if T % i == 0:
                print(i)


main()