def main():
    origem = input('Local de origem: ')
    destino = input('Local de destino: ')

    valor_rs = float(input('Valor em reais no site: '))
    milhas = float(input('Valor em milhas no site: '))

    def percentual(rs, tipo):
        return (tipo / rs) * 100
    

    acumulada = (milhas / 1000) * 14.5
    padrao = (milhas / 1000) * 70
    
    percentual_padrao = percentual(valor_rs, padrao)
    percentual_acumulada = percentual(valor_rs, acumulada)


    print(f'Valor em milhas padrão: {padrao:.2f} R$.')
    print(f'Percentual de milhas padrão em relação ao valor em R$: {percentual_padrao:.2f} %. ')
    print(f'Valor em milhas acumuladas: {acumulada:.2f} R$.')
    print(f'Percentual de milhas acumuladas em relação ao valor em R$: {percentual_acumulada:.2f} %. ')

    if valor_rs < padrao and valor_rs < acumulada:
        print('O valor em R$ é mais indicado.')
    elif padrao < valor_rs and padrao < acumulada:
        print('O valor em milhas padrão é mais indicado.')
    else:
        print('O valor em milhas acumuladas é o mais indicado.')






main()