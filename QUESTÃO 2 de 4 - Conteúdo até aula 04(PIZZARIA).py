print('Bem-vindo a Pizzaria Don Corleone Pacheco')
print('------------------------CARDÁPIO-------------------------')
print('CÓDIGO | DESCRIÇÃO | PIZZA MÉDIA (M) | PIZZA GRANDE (G) |')
print('  21   | Napolitana|   R$: 20,00     |    R$: 26,00     |')
print('  22   | Margherita|   R$: 20,00     |    R$: 26,00     |')
print('  23   | Calabresa |   R$: 25,00     |    R$: 32,50     |')
print('  24   |  Toscana  |   R$: 30,00     |    R$: 39,00     |')
print('  25   | Portuguesa|   R$: 30,00     |    R$: 39,00     |')
print('---------------------------------------------------------')
acumulador = 0
while True:
    tamanho = input('Entre com o tamanho de pizza desejado (M/G): ')
    tamanho = tamanho.upper()
    if tamanho != 'M' and tamanho != 'G':
        print('Opção inválida.')
        continue

    codigo = input('Entre com o codigo de pizza desejado (21/22/23/24/25): ')
    if codigo != '21' and codigo != '22' and codigo != '23' and codigo !='24' and codigo != '25':
        print('Opção inválida.')
        continue

    if codigo == '21' and tamanho == 'M':
        print('Você escolheu a pizza Napolitana tamanho M')
        acumulador = acumulador + 20

    elif codigo == '21' and tamanho == 'G':
        print('Você escolheu a pizza Napolitana tamanho G')
        acumulador = acumulador + 26

    elif codigo == '22' and tamanho == 'M':
        print('Você escolheu a pizza Margherita tamanho M')
        acumulador = acumulador + 20
    
    elif codigo == '22' and tamanho == 'G':
        print('Você escolheu a pizza Margherita tamanho G')
        acumulador = acumulador + 26

    elif codigo == '23' and tamanho == 'M':
        print('Você escolheu a pizza Calabresa tamanho M')
        acumulador = acumulador + 25
    
    elif codigo == '23' and tamanho == 'G':
        print('Você escolheu a pizza Calabresa tamanho G')
        acumulador = acumulador + 32.50

    elif codigo == '24' and tamanho == 'M':
        print('Você escolheu a pizza Toscana tamanho M')
        acumulador = acumulador + 30
    
    elif codigo == '24' and tamanho == 'G':
        print('Você escolheu a pizza Toscana tamanho G')
        acumulador = acumulador + 39

    elif codigo == '25' and tamanho == 'M':
        print('Você escolheu a pizza Portuguesa tamanho M')
        acumulador = acumulador + 30
    
    elif codigo == '25' and tamanho == 'G':
        print('Você escolheu a pizza Portuguesa tamanho G')
        acumulador = acumulador + 39

    pedir_mais =input('Deseja pedir mais alguma pizza (S/digite outra tecla)?: ')
    pedir_mais = pedir_mais.upper()
    if pedir_mais == 'S':
        continue
    else:
        print('O valor total a ser pago: R${:.2f}'.format(acumulador))
        break