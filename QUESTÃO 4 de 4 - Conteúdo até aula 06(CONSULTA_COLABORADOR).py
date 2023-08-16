# Inicialização das variáveis globais
id_global = 1
lista_colaboradores = []

# Função para cadastrar um colaborador
def cadastrar_colaborador(id):
    global id_global
    nome = input("Digite o nome do colaborador: ")
    setor = input("Digite o setor do colaborador: ")
    salario = float(input("Digite o salário do colaborador: "))
    
    colaborador = {"id": id, "nome": nome, "setor": setor, "salario": salario}
    lista_colaboradores.append(colaborador)
    id_global += 1

# Função para consultar os colaboradores
def consultar_colaborador():
    opcao = int(input("Escolha uma opção:\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Setor\n4. Retornar ao menu\n"))
    
    if opcao == 1:
        for colaborador in lista_colaboradores:
            print(colaborador)
    elif opcao == 2:
        id_busca = int(input("Digite o ID do colaborador: "))
        for colaborador in lista_colaboradores:
            if colaborador["id"] == id_busca:
                print(colaborador)
                break
    elif opcao == 3:
        setor_busca = input("Digite o setor a ser consultado: ")
        for colaborador in lista_colaboradores:
            if colaborador["setor"] == setor_busca:
                print(colaborador)
    elif opcao == 4:
        return
    else:
        print("Opção inválida")

# Função para remover um colaborador
def remover_colaborador():
    id_remover = int(input("Digite o ID do colaborador a ser removido: "))
    for colaborador in lista_colaboradores:
        if colaborador["id"] == id_remover:
            lista_colaboradores.remove(colaborador)
            print("Colaborador removido com sucesso.")
            return
    print("ID de colaborador não encontrado.")

# Função principal do programa
def main():
    while True:
        print("\nBem-vindo ao Controle de Colaboradores do Anderson Pacheco!\n")
        opcao_menu = int(input("Escolha uma opção:\n1. Cadastrar Colaborador\n2. Consultar Colaborador\n3. Remover Colaborador\n4. Encerrar Programa\n"))

        if opcao_menu == 1:
            cadastrar_colaborador(id_global)
        elif opcao_menu == 2:
            consultar_colaborador()
        elif opcao_menu == 3:
            remover_colaborador()
        elif opcao_menu == 4:
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()