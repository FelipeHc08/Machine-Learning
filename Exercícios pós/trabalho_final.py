"""
Sistema de Controle de Estoque

Estrutura do Estoque
O estoque será armazenado em um dicionário , onde cada chave representa o nome de um produto (como "Camiseta"),
e o valor associado é outro dicionário contendo:
"quantidade": número inteiro (quantas unidades estão disponíveis).
"valor": número decimal (preço unitário do produto).

Função: Adicionar Produtos ao Estoque
Adiciona uma determinada quantidade de um produto ao estoque.
Se o produto não existe , ele será criado.
Se já existir, a função aumentará a quantidade disponível (sem alterar o valor).

Função: Remover Produtos do Estoque
Remove uma certa quantidade de um produto do estoque.
Se a quantidade a ser removida for maior que a disponível, remove o máximo possível e exibe uma mensagem avisando isso.
Se o produto não existir , mostra uma mensagem de erro.

Função: Buscar Informações de um Produto
Permite pesquisar por um produto específico e obter:
Quantidade disponível.
Valor unitário.
Se o produto não for encontrado, retorna informações vazias.

Função: Remover um Produto Completamente
Remove um produto do estoque de forma definitiva.
Se o produto existir , ele será excluído.
Se não existir , exibe uma mensagem de erro.

Função: Imprimir o Estoque Atual
Mostra todos os produtos do estoque com suas quantidades e valores.
Se o estoque estiver vazio, informa isso ao usuário.
Se houver produtos, imprime cada um com seus dados organizados.

Função: Calcular o Valor Total do Estoque
Calcula o valor total de tudo que está no estoque.
Multiplica a quantidade de cada produto pelo seu valor.
Soma esses valores e retorna o total.
Dessa forma, você sabe quanto vale todo o seu estoque em reais.


No final, coloque em um loop para que o usuário possa escolher entre as funções ou sair do programa.
"""

estoque = dict()


def mostrar_menu():
    print("\n================================CONTROLE DE ESTOQUE====================================================\n")
    print("1. Adicionar produtos")
    print("2. Remover produtos")
    print("3. Buscar produtos")
    print("4. Listar estoque completo")
    print("5. Sair")
    print("\n=======================================================================================================\n")


def obter_opcao():
    return input("Informe a opção desejada: ")


def valida_quantidade(acao):
    while True:
        if acao == 0:
            quantidade_produto = input("Informe a quantidade do produto que deseja adicionar ao estoque: ")
        elif acao == 1:
            quantidade_produto = input("Informe a quantidade do produto que deseja remover do estoque: ")

        try:
            valor = int(quantidade_produto)
            return valor
        except ValueError:
            print("Quantidade inválida!")


def valida_valor():
    while True:
        valor_produto = input("Informe o valor do produto que deseja adicionar ao estoque: ")
        try:
            valor = float(valor_produto)
            if valor > 0:
                return valor
        except ValueError:
            print("Valor inválido!")


def formatar_nome(nome):
    return nome.capitalize()


def produto_cadastrado(nome_produto):
    if nome_produto in estoque:
        return True
    else:
        return False


def buscar_produto_estoque(nome_produto, tem_produto):
    if tem_produto:
        return exibir_produto(nome_produto)
    else:
        return print("PRODUTO NÃO ENCONTRADO!")


def exibir_estoque():
    if not estoque:
        print("ESTOQUE VAZIO.")
        return

    print("ESTOQUE COMPLETO:")
    print("-" * 30)
    for produto, info in estoque.items():
        print(f"Produto: {produto}")
        print(f"Quantidade: {info['Quantidade']}")
        print(f"Valor unitário: R$ {info['Valor']:.2f}")
        print("-" * 30)


def exibir_produto(nome_produto):
    print("-" * 30)
    print(f"Produto: {nome_produto}")
    print(f"Quantidade: {estoque[nome_produto]['Quantidade']}")
    print(f"Valor unitário: R$ {estoque[nome_produto]['Valor']:.2f}")
    print("-" * 30)


def deletar_produto(nome_produto, quantidade_produto):
    if nome_produto in estoque:
        if quantidade_produto >= estoque[nome_produto]["Quantidade"]:
            del estoque[nome_produto]
            print(f"Produto '{nome_produto}' apagado do estoque.")
        elif quantidade_produto < estoque[nome_produto]["Quantidade"]:
            estoque[nome_produto]["Quantidade"] -= quantidade_produto
            print(f"Foram removidas {quantidade_produto} unidades de {nome_produto}. "
                  f"Total registrado: {estoque[nome_produto]['Quantidade']} unidades")

    else:
        print("Produto não encontrado")


def valida_nome():
    while True:
        nome_produto = input("Informe o nome do produto: ")

        if not nome_produto:
            print("Nome não pode estar vazio!")
            continue

        if all(c.isalpha() or c.isspace() for c in nome_produto):
            nome_produto = formatar_nome(nome_produto)
            return nome_produto
        else:
            print("Nome inválido!")


def adicionar_produto(nome_produto, quantidade_produto, valor_produto):
    estoque[nome_produto] = dict()
    estoque[nome_produto]["Quantidade"] = quantidade_produto
    estoque[nome_produto]["Valor"] = valor_produto


def alterar_quantidade(nome_produto):
    quantidade_a_adicionar = valida_quantidade(0)
    estoque[nome_produto]["Quantidade"] += quantidade_a_adicionar


def calcular_valor_estoque():
    total = 0
    for produto in estoque.values():
        total += produto["Quantidade"] * produto["Valor"]
    return total


def valida_opcao(opcao):
    try:
        opcao = int(opcao)
        if opcao == 1:
            print("ADICIONAR PRODUTO")
            nome_produto = valida_nome()
            if produto_cadastrado(nome_produto):
                print("Produto já cadastrado")
                alterar_quantidade(nome_produto)
            else:
                quantidade_valida = valida_quantidade(0)
                valor_valido = valida_valor()
                valor_total_produto = float(quantidade_valida * valor_valido)
                calcular_valor_estoque()
                adicionar_produto(nome_produto, quantidade_valida, valor_valido)

        elif opcao == 2:
            print("DELEÇÃO DE PRODUTO")
            nome_produto = valida_nome()
            quantidade_produto = valida_quantidade(1)
            deletar_produto(nome_produto, quantidade_produto)
        elif opcao == 3:
            print("BUSCA DE PRODUTO")
            nome_produto = valida_nome()
            buscar_produto_estoque(nome_produto, produto_cadastrado(nome_produto))

        elif opcao == 4:
            exibir_estoque()
            print(f"Soma total no estoque: R$ {calcular_valor_estoque():.2f}")

        elif opcao == 5:
            return True

        else:
            print("Opção inválida!")
            return False
        return True

    except ValueError:
        print("Entrada inválida! Digite um número de 1 a 5.")
        return False


while True:
    mostrar_menu()
    entrada = obter_opcao()
    if valida_opcao(entrada):
        if int(entrada) == 5:
            print("ENCERRANDO PROGRAMA...")
            break
