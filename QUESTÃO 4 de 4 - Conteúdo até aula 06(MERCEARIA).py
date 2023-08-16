# -------------------- Inicio das Variáveis Globais --------------------
lista_produto = []
codigo_produto = 0

# -------------------- Fim das variáveis GLobais --------------------

# -------------------- Inicio de cadastrar_produto() --------------------
def cadastrar_produto(codigo):
    print('Bem-vindo ao menu de Cadastrar Produto')
    print('Codigo do Produto: {}'.format(codigo))
    nome = input('Entre com o NOME do Produto: ')
    fabricante = input('Entre com o FABRICANTE do Produto: ')
    preco = int(input('Entre com o PREÇO(R$) do produto: '))
    dicionario_produto = {'codigo'      : codigo,
                          'nome'        : nome,
                          'fabricante'  : fabricante,
                          'preco'       : preco}
    lista_produto.append(dicionario_produto.copy())
# -------------------- Fim de cadastrar_produto() --------------------


# -------------------- Inicio de consultar_produtos() --------------------
def consultar_produto():
    print('Bem-vindo ao menu de Consultar Produto')
    while True:
        opcao_consultar = input('\nEscolha a opção desejada:\n'+
                                '1-Consultar TODOS os Produtos\n'+
                                '2-Consultar Produto por CÓDIGO\n'+
                                '3-Consultar produto(s) por FABRICANTE\n'+
                                '4-Retornar\n'+
                                '>>')
        if opcao_consultar == '1':
            print('Você escolheu a opção consultar TODOS os produtos')
            for produto in lista_produto: #produto vai varrer toda lista de produtos
                print('------------------------------')
                for key, value in produto.items(): #varrer todos os conjuntos chaves e valor do dicionario produto 
                    print('{}: {}'.format(key,value))
                print('------------------------------')
        elif opcao_consultar == '2':
            print('Você escolheu a opção consultar Produto por CÓDIGO')
            valor_desejado = int(input('Entre com o CÓDIGO desejado: '))
            for produto in lista_produto:
                if produto['codigo'] == valor_desejado: # o valor do campo código desse dicionário é igual o valor desejado
                    print('------------------------------')
                    for key, value in produto.items(): #varrer todos os conjuntos chaves e valor do dicionario produto 
                        print('{}: {}'.format(key,value))
                print('------------------------------')

        elif opcao_consultar == '3':
            print('Você escolheu a opção consultar produto(s) por FABRICANTE')
            valor_desejado = input('Entre com o FABRICANTE desejado: ')
            for produto in lista_produto:
                if produto['fabricante'] == valor_desejado: # o valor do campo código desse dicionário é igual o valor desejado
                    print('------------------------------')
                    for key, value in produto.items(): #varrer todos os conjuntos chaves e valor do dicionario produto 
                        print('{}: {}'.format(key,value))
                print('------------------------------')
        elif opcao_consultar == '4':
            return #sai da função consultar_produto e volta para Main
        else:
            print('Opção Inválida. Tente novamente.')
            continue #volta para o inicio do laço

# -------------------- Fim de consultar_produto() --------------------

# -------------------- Inicio de remover_produto() --------------------
def remover_produto():
    print('Bem-vindo ao menu de Remover Produto')
    valor_desejado = int(input('Entre com o código do produto que deseja remover: '))
    for produto in lista_produto:
        if produto['codigo'] == valor_desejado:
            lista_produto.remove(produto)
            print('Produto removido')
# -------------------- Fim de remover_produto() --------------------

# -------------------- Inicio de Main() --------------------
print('Bem-vindo a mercearia Anderson')
while True:
    opcao_principal = input('\nEscolha a opção desejada:\n'+
                            '1-Cadastrar Produto\n'+
                            '2-Consultar Produto(s)\n'+
                            '3-Remover Produto\n'+
                            '4-Sair\n'+
                            '>>')
    if opcao_principal == '1':
        codigo_produto = codigo_produto + 1
        cadastrar_produto(codigo_produto)
    elif opcao_principal == '2':
        consultar_produto()
    elif opcao_principal == '3':
        remover_produto()
    elif opcao_principal == '4':
        break #encerra o laço principal e o programa acaba
    else:
        print('Opção Inválida. Tente novamente.')
        continue #volta para o inicio do laço

# -------------------- Fim de Main() --------------------