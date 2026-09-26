
import os

restaurantes = [{'nome':'Praça', 'categoria':'Japnesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria': 'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False},
                ]
def exibir_nome_do_programa():
    '''Exibe o logotipo e o titulo estilizado do programa no terminal.'''
    print("""

██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
""")

def exibir_opcoes():
    '''Exibe o menu de opção disponiveis para o usuário no terminal.'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Exibe a mensagem de encerramento da aplicação no terminal.'''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite um tecla para voltar ao menu')
    main()

def opcao_invalida():
    '''
    Exibe mensagens de opção inválida e redireciona o usuário para 
    o menu princial.
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Limpa o console e exibe o texto informado formatado entre
    linas divisórias.'''
    os.system('cls')
    linha = '-' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função e responsavel por cadastra um novo 
    restaurante
    
    imputs:
    - Nome dos restaurantes 
    - Categoria

    output:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')   
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante) 
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''
    Exibe no terminal a lista dormata de todos os restaurante 
    cadastrado com seus status.
    '''
    exibir_subtitulo('Listando restaurantes')
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}' )

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Busca um restaurante pelo nome e inverte o seu estado de
    ativação.'''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterna o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {restaurante["nome"]} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {restaurante["nome"]} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Captura a escolha do usuário no menu e direciona o fluxo para
    a função correspondente.'''
    try:
        opcao_escolhida = int(input('Escolha uma opção:  '))
        

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == :
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Inicia a aplicação, limpa a tela e apresenta o menu
    principal.'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()