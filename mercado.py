from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('========================')
    print('======Bem-Vindo(a)======')
    print('======CarlShopping======')
    print('========================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produtos')
    print('3 - Comprar Produtos')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair do Sistema')

    opcao: int = int(input('Digite a opção desejada aqui: '))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre às compras! Nos vemos em breve. . .')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida! Tente novamente')
        sleep(2)
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('===================')

    nome: str = input('Digite o nome do produto: ').strip().title()
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Lista de Produtos')
        print('-----------------')
        for produto in produtos:
            print(produto)
            print('-----------------')
            sleep(1)
    else:
        print('Nenhum produto foi cadastrado!')
        sleep(2)
        menu()
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto desejado')
        print('====== Produtos Cadastrados ========')

        for produto in produtos:
            print(produto)
            sleep(1)
        
        codigo : int = int(input('Digite o código aqui: '))

        produto : Produto = verifica_produto_por_codigo(codigo)
        if produto:
            if len(carrinho) > 0:
                produto_repetido : bool = False
                for unidade in carrinho:
                    quantidade_do_produto : int = unidade.get(produto)
                    if quantidade_do_produto:
                        unidade[produto] = quantidade_do_produto + 1 #Esse +1 é o exemplar que o cliente comprou agora
                        print(f'O produto {produto.nome} agora tem {quantidade_do_produto + 1} unidades')
                        produto_repetido = True
                        sleep(2)
                        menu()
                if not produto_repetido: #Se o produto não estiver no carrinho
                    produto_comprado = {produto: 1}
                    carrinho.append(produto_comprado)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho')
                    sleep(2)
                    menu()
            else:
                carrinho.append(produto)
                print(f'O produto {produto.nome} foi adicionado ao carrinho de compras!')
                sleep(2)
                menu()
        else:
            print('O código informado é inválido. Tente novamente!')
            sleep(2)
            menu()
    else:
        print('Ainda não há produtos disponíveis para venda no sistema')
        sleep(2)
        menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(f'O produto: {dados[0]} tem {dados[1]} unidades no carrinho')
                sleep(2)
                menu()
                
    else:
        print('Ainda não há produtos no carrinho. Adicione produtos para vê-los')
        sleep(2)
        menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total : float = 0

        print('Produtos do Carrinho')
        print('--------------------')
        
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('--------------------')
                sleep(1.5)
            sleep(1)
            print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
            print('Volte sempre!')
            
            carrinho.clear()
            sleep(5)
    else:
        print('Ainda não existem produtos no carrinho')
        sleep(2)
        menu()


def verifica_produto_por_codigo(codigo_do_produto: int) -> Produto:
    verificar_produto : Produto = None

    for produto in produtos:
        if produto.codigo == codigo_do_produto:
            verificar_produto = produto
    return verificar_produto


if __name__ == '__main__':
    main()
