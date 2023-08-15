# Função para obter o peso do cachorro

def cachorro_peso():

   while True:
       try:
           peso = float(input('Digite o peso do seu Pet (em kg): '))
           if peso < 3:
               return 40
           elif peso < 10:
               return 50
           elif peso < 30:
               return 60
           elif peso < 50:
               return 70
           else:
               print('Não aceitamos Pet tão grandes \n'
                     'Por favor, entre com o peso do seu Pet novamente. \n')
       except ValueError:
           print('Você digitou um valor não numérico. \n'
                 'Por favor, entre com o peso do seu Pet novamente. \n')

# Função para obter o tipo de pelo do cachorro

def cachorro_pelo():

   while True:
       pelo = input('Digite o tipo de pelo do seu Pet: \n'
                    'c - Pelo Curto \n'
                    'm - Pelo Médio \n'
                    'l - Pelo Longo \n').lower()
       if pelo == 'c':
           return 1
       elif pelo == 'm':
           return 1.5
       elif pelo == 'l':
           return 2
       else:
           print('Opção Inválida \n'
                 'Digite c/m/l \n')
                 
# Função para obter os serviços adicionais

def cachorro_extra():

   valor_extra = 0
   while True:
       try:
           adicional = int(input('Deseja adicionar mais algum serviço? \n'
                                 '1 - Corte de Unhas - R$: 10,00 \n'
                                 '2 - Escovar Dentes - R$: 12,00 \n'
                                 '3 - Limpeza de Orelhas - R$: 15,00 \n'
                                 '0 - Não desejo mais nada \n' +
                                 '>>'))
           if adicional == 0:
               break
           elif adicional == 1:
               valor_extra += 10
           elif adicional == 2:
               valor_extra += 12
           elif adicional == 3:
               valor_extra += 15
           else:
               print('Opção inválida. Tente novamente.')
       except ValueError:
           print('Valor inválido. Tente novamente.')
   return valor_extra

# Função principal

def main():
   print('Bem-vindo(a) ao sistema de cobrança do Petshop!')
   nome = input('Digite o seu nome: ')

   print('Olá,', nome,'seja bem-vindo')
   
   base = cachorro_peso()

   multiplicador = cachorro_pelo()

   extra = cachorro_extra()

   total = base * multiplicador + extra

   print("O valor total da conta é: R$", total)

# Execução do programa

if __name__ == '__main__':

   main()