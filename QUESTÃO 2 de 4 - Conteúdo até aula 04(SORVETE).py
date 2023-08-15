# [EXIGÊNCIA] - A - Print uma mensagem de boas-vindas
print('Bem-vindo a Sorveteria Anderson Pacheco')
print('-----------------------------------CARDÁPIO--------------------------------------')
print('Nº DE BOLAS | SABOR TRADICIONAL (tr) | SABOR PREMIUM (pr) | SABOR ESPECIAL (es) |')
print('     1      |        R$: 6,00        |      R$: 7,00      |      R$: 8,00       |')
print('     2      |        R$: 10,00       |      R$: 12,00     |      R$: 14,00      |')
print('     3      |        R$: 14,00       |      R$: 17,00     |      R$: 20,00      |')
print('---------------------------------------------------------------------------------')
vl_tr_1 = 6
vl_pr_1 = 7
vl_es_1 = 8
vl_tr_2 = 10
vl_pr_2 = 12
vl_es_2 = 14
vl_tr_3 = 14
vl_pr_3 = 17
vl_es_3 = 20
acumulador = 0

#[EXIGÊNCIA] B - ENTRADA SABOR E NÚMERO DE BOLAS DE SORVETE
while True:
    sabor = input('Entre com o sabor desejado (tr/pr/es): ')
    sabor = sabor.upper()

#[EXIGÊNCIA] D - SABOR INVÁLIDO AO DIGITAL VALOR DA VARIAVEL DIFERENTE DO MENCIONADO
    if sabor != 'TR' and sabor != 'PR' and sabor != 'ES':
        print('Sabor inválido. Tente novamente')
        continue

#[EXIGÊNCIA] C - NÚMERO DE BOLAS INVÁLIDO AO DIGITAL VALOR DA VARIAVEL DIFERENTE DO MENCIONADO
    numb = input('Entre com o número de bolas de sorvete desejado (1/2/3): ')
    if numb != '1' and numb != '2' and numb != '3':
        print('Número de bolas de sorvete inválido. Tente novamente')
        continue

    if numb == '1' and sabor == 'TR':
        print('Você pediu 1 bola de sorvete no sabor TRADICIONAL: R$ {:.2f}'.format(vl_tr_1))
        acumulador = acumulador + 6

    elif numb == '1' and sabor == 'PR':
        print('Você pediu 1 bola de sorvete no sabor PREMIUM: R$ {:.2f}'.format(vl_pr_1))
        acumulador = acumulador + 7

    elif numb == '1' and sabor == 'ES':
        print('Você pediu 1 bola de sorvete no sabor ESPECIAL: R$ {:.2f}'.format(vl_es_1))
        acumulador = acumulador + 8

    elif numb == '2' and sabor == 'TR':
        print('Você pediu 2 bolas de sorvete no sabor TRADICIONAL: R$ {:.2f}'.format(vl_tr_2))
        acumulador = acumulador + 10

    elif numb == '2' and sabor == 'PR':
        print('Você pediu 2 bolas de sorvete no sabor PREMIUM: R$ {:.2f}'.format(vl_pr_2))
        acumulador = acumulador + 12

    elif numb == '2' and sabor == 'ES':
        print('Você pediu 2 bolas de sorvete no sabor ESPECIAL: R$ {:.2f}'.format(vl_es_2))
        acumulador = acumulador + 14

    elif numb == '3' and sabor == 'TR':
        print('Você pediu 3 bolas de sorvete no sabor TRADICIONAL: R$ {:.2f}'.format(vl_tr_3))
        acumulador = acumulador + 14

    elif numb == '3' and sabor == 'PR':
        print('Você pediu 3 bolas de sorvete no sabor PREMIUM: R$ {:.2f}'.format(vl_pr_3))
        acumulador = acumulador + 17

    elif numb == '3' and sabor == 'ES':
        print('Você pediu 3 bolas de sorvete no sabor ESPECIAL: R$ {:.2f}'.format(vl_es_3))
        acumulador = acumulador + 20

#[EXIGÊNCIA] E - PERGUNTAR AO CLIENTE SE DESEJA PEDIR MAIS ALGUMA COISA
    pedir_mais =input('Deseja mais algum sorvete? (s/digite outra tecla)?: ')
    pedir_mais = pedir_mais.upper()
    if pedir_mais == 'S':
        continue
    else:
        print('O valor total a ser pago: R${:.2f}'.format(acumulador))
        break