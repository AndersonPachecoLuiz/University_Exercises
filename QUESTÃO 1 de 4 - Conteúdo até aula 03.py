# Passo A - [Print boas vindas.]
print('Seja muito bem-vindo(a) ao programa de cálculo de desconto - Anderson Pacheco Cosmetics.')

# Passo B - [Entrada de valor unitário e quantidade.]
valor_produto = float(input('Digite o valor unitário do produto: '))
qtd_produto = int(input('Digite a quantidade desejada do produto: '))
desconto_produto = 0

# Passo D - [Utilização das estruturas if, elif e else.]
if qtd_produto <= 199:
    desconto_produto = 0.00
elif 200 <= qtd_produto < 1000:
    desconto_produto = 0.05
elif 1000 <= qtd_produto < 2000:
    desconto_produto = 0.10
else:
    desconto_produto = 0.15

# Passo C - [Retorno do valor total sem desconto e retorno do valor total com desconto.]
# Passo F - [Apresentação de saída no console]
total_sem_desconto = valor_produto * qtd_produto
print('O valor total sem desconto é de: R$ {: .2f}' .format(total_sem_desconto))
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
print('O valor total com desconto é de: R$ {: .2f}' .format(total_com_desconto))
desconto_produto = int(desconto_produto * 100)
print(f"Você recebeu {desconto_produto}% de desconto. ")
valor_desconto = total_sem_desconto - total_com_desconto
print('O seu desconto é de R$ {: .2f}' .format(valor_desconto))