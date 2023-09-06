########################################################################################################################
# IA AND MACHINE LEARNING - CHECKPOINT 1
# prof: Hellynson Cassio Lana
# Turma: 2TCNR-2023
#
# Grupo: Cloud Hub
#
# Integrantes:
# Andrew Pereira Nogueira   – RM 93103
# Guilherme de Oliveira     – RM 92952
# Lucas S. de Castilhos     – RM 93538
# Ronaldo Prates            – RM 93601
# Ronaldo Volcov            – RM 84422
#
# - Features
# - Login e senha
# - Senha oculta ao digitar
# - Geração do #id automático
# - Mostrar Usuário Logado e nível
# - Códigos de Sistema pode ser digitados em qualquer ponto quando solicitado:
# - Formatação simples da listagem
# - Exibição do item a ser editado
# - Edição de Item por campo
# - Menu de vendas apenas disponivel para o nivel/perfil de vendas
# - Menu de gerenciar usuários apenas disponivel para o nivel/perfil de admin

########################################################################################################################
from getpass import getpass

########################################################################################################################
produtos = []
clientes = []
vendas = []

usuarioLogado = {}

produtoAutoIncrement = 1
clienteAutoIncrement = 1
vendasAutoIncrement = 1

usuarios = [
    {
        "nome": "Andrew Pereira Nogueira",
        "login": "93103",
        "senha": "93103",
        "nivel": ["CADASTRO"]
    },
    {
        "nome": "Guilherme de Oliveira",
        "login": "92952",
        "senha": "92952",
        "nivel": ["VENDAS"]
    },
    {
        "nome": "Lucas Sussin",
        "login": "93538",
        "senha": "93538",
        "nivel": ["VENDAS"]
    },
    {
        "nome": "Ronaldo Prates",
        "login": "93601",
        "senha": "93601",
        "nivel": ["ADMIN", "VENDAS"]
    },
    {
        "nome": "Ronaldo Volcov",
        "login": "84422",
        "senha": "84422",
        "nivel": ["CADASTRO"]
    }
]


########################################################################################################################
def get_produto_auto_increment():
    global produtoAutoIncrement
    produtoAutoIncrement += 1
    return produtoAutoIncrement


def get_cliente_auto_increment():
    global clienteAutoIncrement
    clienteAutoIncrement += 1
    return clienteAutoIncrement


########################################################################################################################

def mascara_valor_em_real(value):
    a = '{:,.2f}'.format(float(value))
    b = a.replace(',', 'v')
    c = b.replace('.', ',')
    return c.replace('v', '.')


def formatar_moeda_de_real_para_padrao(value):
    return value.replace('.', '').replace(',', '.')  # 1.000,00


########################################################################################################################
def verifica_permissao_usuario_logado_vendas():
    return verifica_permissao_usuario_logado("VENDAS")


def verifica_permissao_usuario_logado_admin():
    return verifica_permissao_usuario_logado("ADMIN")


def verifica_permissao_usuario_logado(nivel):
    for n in usuarioLogado["nivel"]:
        if n == nivel:
            return True

    return False


########################################################################################################################
def exibir_produto(produto):
    print("\n ID: {} \n Nome: {} \n Descrição: {} \n Preço: R$ {} \n".format(
        produto['id'],
        produto['nome'],
        produto['descricao'],
        mascara_valor_em_real(produto['preco'])))


def exibir_cliente(cliente):
    (print("Valor atual do registro: "))
    print("\n ID: {} \n Nome: {} \n CPF: {} \n TELEFONE: {} \n".format(
        cliente['id'],
        cliente['nome'],
        cliente['cpf'],
        cliente['telefone']))


########################################################################################################################
def deslogar():
    global usuarioLogado
    print("Deslogando o usuário {}".format(usuarioLogado["nome"]))
    usuarioLogado = {}
    logar()


########################################################################################################################

def entrada(mensagem):
    filtro = input(mensagem)

    match str(filtro):
        case "#0":
            sair()
            exit()
        case "#9":
            deslogar()
        case "#menu":
            menu_principal()
        case "#menu#efetuar_venda":
            efetuar_venda()

    return filtro


########################################################################################################################

def logar():
    while True:
        print("\n:: LOGIN :: Empório Barnabé")
        login = entrada("Login: ")
        senha = getpass("Senha: ")

        for usuario in usuarios:
            if usuario["login"] == login and usuario["senha"] == senha:
                global usuarioLogado
                usuarioLogado = usuario
                print("\n Usuário encontrado... Redirecionando para o menu! \n")
                menu_principal()
                return False

        print("Login e/ou senha inválidos! Tente novamente ou entre em contato com um administrador")


########################################################################################################################


def menu_principal():
    while True:
        print(":: Sistema Empório Barnabé :: Menu Princpal :: Usuário logado [{} - {}] \n "
              .format(usuarioLogado["nome"], usuarioLogado["nivel"]))

        print("[1] Cadastrar um Produto")
        print("[2] Listar Produtos")
        print("[3] Editar Produto")

        print("[4] Cadastrar Cliente")
        print("[5] Listar clientes")
        print("[6] Editar Cliente")

        if verifica_permissao_usuario_logado_vendas():
            print("[7] Efetuar uma Venda")
            print("[8] Listar Vendas")

        if verifica_permissao_usuario_logado_admin():
            print("[9] Gerenciar Usuários")

        print("[0] Logout")

        opcao = entrada("\nEscolha uma opção: ")

        match opcao:
            case "1":
                cadastrar_produto()
            case "2":
                listar_produtos()
            case "3":
                editar_produto()
            case "4":
                cadastrar_cliente()
            case "5":
                listar_clientes()
            case "6":
                editar_cliente()
            case "7":
                if verifica_permissao_usuario_logado_vendas():
                    efetuar_venda()
            case "8":
                if verifica_permissao_usuario_logado_vendas():
                    listar_vendas()
            case "9":
                if verifica_permissao_usuario_logado_admin():
                    listar_usuarios()
            case "0":
                deslogar()
            case _:
                print("Opção inválida!")


########################################################################################################################
def cadastrar_produto():
    print("\n:: CADASTRO DE PRODUTO")

    produtos.append(dict({
        "id": "P0000{}".format(get_produto_auto_increment()),
        "nome": entrada("Digite o nome do produto: ".format()),
        "descricao": entrada("Digite a descrição do produto: "),
        "preco": formatar_moeda_de_real_para_padrao(entrada("Digite o preço do produto: R$ "))
    }))

    print("Produto cadastrado com sucesso!")

    listar_produtos()


def cadastrar_cliente():
    print(":: CADASTRO DE CLIENTES ")

    clientes.append(dict({
        "id": "C0000{}".format(get_cliente_auto_increment()),
        "nome": entrada("Digite o nome do cliente: "),
        "cpf": entrada("Digite a cpf do cliente: "),
        "telefone": entrada("Digite o telefone do cliente: ")
    }))

    print("Cliente cadastrado com sucesso!")

    listar_clientes()


########################################################################################################################
def efetuar_venda():
    print("\n:: EFETUAR DE VENDA ")

    if (not len(clientes)) or (not len(produtos)):
        print("Não há clientes e/ou produtos cadastrados para lançar uma venda!")
        menu_principal()

    venda = {
        "id": {
            "cpf_cliente": entrada("Digite a cpf do cliente: "),
            "nome_produto": entrada("Digite o nome do produto: ")
        }
    }

    for v in vendas:
        if v["id"]["cpf_cliente"] == venda["id"]["cpf_cliente"] \
                and v["id"]["nome_produto"] == venda["id"]["nome_produto"]:
            print("Já existe uma venda lançada para este cliente & produto")
            efetuar_venda()

    cliente_valido = False
    produto_valido = False

    for c in clientes:
        if c["cpf"] == venda["id"]["cpf_cliente"]:
            cliente_valido = True

    for p in produtos:
        if p["nome"] == venda["id"]["nome_produto"]:
            produto_valido = True

    if (not cliente_valido) or (not produto_valido):
        print("CPF ou Produto inexistente!")
        efetuar_venda()
    vendas.append(venda)

    print("Venda lançada com sucesso!")

    listar_vendas()


########################################################################################################################
def listar_produtos():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado!\n")
        return

    print("+---------------------------------------------------------|")
    print("| {:1} | {:6} | {:8} | {:17} | {:11} |".format("#", "ID", "NOME", "DESCRIÇÃO", "PREÇO"))
    print("+---------------------------------------------------------|")
    for i, produto in enumerate(produtos):
        print("| {:1} | {:1} | {:1} | {:1} | R$ {:1} |".format(
            i + 1,
            produto['id'],
            produto['nome'],
            produto['descricao'],
            mascara_valor_em_real(produto['preco'])))
    print("+---------------------------------------------------------|")
    print("| Total de Registros: {} ".format(len(produtos)))
    print("+---------------------------------------------------------|")


def listar_clientes():
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado!\n")
        return

    print("+---------------------------------------------------------|")
    print("| {:1} | {:6} | {:8} | {:11} | {:11} |".format("#", "ID", "NOME", "CPF", "TELEFONE"))
    print("+---------------------------------------------------------|")
    for i, cliente in enumerate(clientes):
        print("| {:1} | {:1} | {:1} | {:1} | {:1} |".format(
            i + 1,
            cliente['id'],
            cliente['nome'],
            cliente['cpf'],
            cliente['telefone']))
    print("+---------------------------------------------------------|")
    print("| Total de Registros: {} ".format(len(clientes)))
    print("+---------------------------------------------------------|")


def listar_vendas():
    if len(vendas) == 0:
        print("Nenhuma venda lançada!\n")
        return

    print("+---------------------------------------------------------|")
    print("| {:1} | {:6} | {:8} |".format("#", "NOME", "CPF"))
    print("+---------------------------------------------------------|")
    for i, venda in enumerate(vendas):
        print("| {:1} | {:1} | {:1} |".format(
            i + 1,
            venda["id"]['cpf_cliente'],
            venda["id"]['nome_produto']))
    print("+---------------------------------------------------------|")
    print("| Total de Registros: {} ".format(len(vendas)))
    print("+---------------------------------------------------------|")


def listar_usuarios():
    print("+---------------------------------------------------------|")
    print("| {:1} | {:6} | {:8} | {:8} |".format("#", "NOME", "LOGIN", "NÍVEL"))
    print("+---------------------------------------------------------|")
    for i, usuario in enumerate(usuarios):
        print("| {:1} | {:1} | {:1} | {:1} |".format(
            i + 1,
            usuario['nome'],
            usuario['login'],
            str(usuario['nivel']).replace("[", "").replace("]", "")
        ))
    print("+---------------------------------------------------------|")
    print("| Total de Registros: {} ".format(len(usuarios)))
    print("+---------------------------------------------------------|")


########################################################################################################################
def editar_produto():
    print(":: EDIÇÃO DE PRODUTO ")
    listar_produtos()

    index = int(entrada("Digite qual produto deseja editar: ")) - 1

    if index < 0 or index >= len(produtos):
        print("Produto inválido!")
        return

    while True:
        exibir_produto(produtos[index])
        print("Qual campo deseja alterar?")
        print("[1] Editar Nome")
        print("[2] Editar Descrição")
        print("[3] Editar Preço")
        print("[0] Voltar")

        opcao = entrada("Digite o código referente ao [{}] campo que deseja alterar: ".format(produtos[index]["nome"]))

        match opcao:
            case "1":
                produtos[index]["nome"] = entrada("Digite o novo Nome: ")
            case "2":
                produtos[index]["descricao"] = entrada("Digite a nova Descrição: ")
            case "3":
                produtos[index]["preco"] = formatar_moeda_de_real_para_padrao(entrada("Digite o novo preço: R$ "))
            case "0":
                return False

        listar_produtos()


def editar_cliente():
    print(":: EDIÇÃO DE CLIENTE ")
    listar_clientes()

    index = int(entrada("Digite qual cliente deseja editar: ")) - 1

    if index < 0 or index >= len(clientes):
        print("Cliente inválido!")
        return

    while True:
        exibir_cliente(clientes[index])
        print("Qual campo deseja alterar?")
        print("[1] Editar Nome")
        print("[2] Editar CPF")
        print("[3] Editar Telefone")
        print("[0] Voltar")

        opcao = entrada("Digite o código referente ao [{}] campo que deseja alterar: ".format(clientes[index]["nome"]))

        match opcao:
            case "1":
                clientes[index]["nome"] = entrada("Digite o novo Nome: ")
            case "2":
                clientes[index]["cpf"] = entrada("Digite a nova CPF: ")
            case "3":
                clientes[index]["telefone"] = formatar_moeda_de_real_para_padrao(entrada("Digite o novo Telefone "))
            case "0":
                return False

        listar_clientes()


########################################################################################################################

def sair():
    print("Obrigado por usar nosso sistema! bye!")
    exit()


#######################################################################################################################
# INICIAR
#######################################################################################################################
logar()
