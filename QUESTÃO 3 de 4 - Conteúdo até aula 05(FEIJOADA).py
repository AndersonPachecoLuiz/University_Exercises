# QUESTÃO 3 de 4 - Conteúdo até aula 05(FEIJOADA)

#Inicio da função volumeFeijoada()
def volumeFeijoada():
    print('------------------------- MENU 1 de 3 - Volume Feijoada ------------------------')
    while True:
        try:
            volumeF = int(input('Digite a quantidade desejada (ml): '))
            if (volumeF >= 300) and (volumeF <= 5000):
                return volumeF * 0.08
            else:
                print('Para de digitar valores abaixo de 300 ou acima de 5000.')
                continue # Retorna para a pergunta
        except ValueError: #Caso o usuário digite carcteres errado
            print('Pare de digitar valores não inteiros')
#Fim da função volumeFeijoada()

#Inicio da função opcaoFeijoada()
def opcaoFeijoada():
    print('------------------------- MENU 2 de 3 - Volume Feijoada ------------------------')
    while True:
        opcaoF = input('Qual a opção de feijoada você deseja? \n' +
                       'b - Básica (Feijão + Paiol + costelinha) \n' +
                       'p - Premium (Feijão + Paiol + costelinha + partes de porco) \n' +
                       's - Suprema (Feijão + Paiol + costelinha + partes de porco + charque + calabresa + bacon) \n' +
                       '>> ')
        opcaoF = opcaoF.lower()
        opcaoF = opcaoF.strip()
        if opcaoF == 'b':
            return 1.00
        elif opcaoF == 'p':
            return 1.25
        elif opcaoF == 's':
            return 1.50
        else:
            print('Pare de digitar opções diferentes de b/p/s')
            continue # Volta para o inicio


##Fim da função volumeFeijoada()

#Inicio da função acompanhamentoFeijoada()
def acompanhamentoFeijoada():
    print('------------------------- MENU 3 de 3 - Volume Feijoada ------------------------')
    acumulador = 0
    while True:
        acompanhamentoF = input('Deseja mais algum adicional: \n' +
                                '0 - Não desejo mais acompanhamentos (encerrar pedido) \n' +
                                '1 - 200g de arroz \n' +
                                '2 - 150g de farofa especial \n' +
                                '3 - 100g de couve cozida \n' +
                                '4 - 1 laranja descascada \n' +
                                '>>')
        if acompanhamentoF == '0':
            return acumulador
        elif acompanhamentoF == '1':
            acumulador = acumulador + 5
            continue # Volta para o inicio do While True
        elif acompanhamentoF == '2':
            acumulador = acumulador + 6
            continue # Volta para o inicio do While True
        elif acompanhamentoF == '3':
            acumulador = acumulador + 7
            continue # Volta para o inicio do While True
        elif acompanhamentoF == '4':
            acumulador = acumulador + 3
            continue # Volta para o inicio do While True
        else:
            print('Pare de digitar opções diferentes de 0/1/2/3/4!')
                    
#Fim da função acompanhamentoFeijoada()

#Inicio da Main

print('---------- Bem-vindo ao programa de Feijoada do Anderson Pacheco Luiz ---------- \n')
volume = volumeFeijoada()
opcao = opcaoFeijoada()
acompanhamento = acompanhamentoFeijoada()
total = (volume * opcao) + acompanhamento
print('O total ficou: R$ {:.2f} (Volume: R$ {:.2f}, Opção: R$ {:.2f}, Acompanhamento: R$ {:.2f},'.format(total,volume,opcao,acompanhamento))