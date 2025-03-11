# - A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
# - Deve ser possível adicionar um contato
#     - O contato pode ter os dados:
#     - Nome
#     - Telefone
#     - Email
#     - Favorito (está opção é para poder marcar um contato como favorito)
contatos = [
    {
         "name": "Erick",
         "phone": "11941412494",
         "email": "ex@email.com",
         "favorite": True
     },
     {
         "name": "Ronaldo",
         "phone": "11941412494",
         "email": "ex@email.com",
         "favorite": False
     },
]
# - Deve ser possível visualizar a lista de contatos cadastrados
def visualizarContatos():
    contatos_quantidades = 0
    for contato in contatos:
        contatos_quantidades += 1
        nome = contato["name"]
        telefone = contato["phone"]
        email = contato["email"]
        favorito = "Sim" if contato["favorite"] == True else "Não"
        print("\nContatos\n")
        print(f"Contato {contatos_quantidades}")
        print(f"Nome: {nome} | Telefone: {telefone}")
        print(f"Email: {email} | Favorito: {favorito}")
        print("----------------------------------------------")

# - Deve ser possível editar um contato
def editarContato(idx_contato, chave_alterar, valor_alterar):
    contato_alterar = contatos[idx_contato-1]
    if chave_alterar == 1:
        contato_alterar["name"] = valor_alterar
        print(f"Nome alterado para {valor_alterar}\n")
    elif chave_alterar == 2:
        contato_alterar["phone"] = valor_alterar
        print(f"Telefone alterado para {valor_alterar}\n")
    elif chave_alterar == 3:
        contato_alterar["email"] = valor_alterar
        print(f"Email alterado para {valor_alterar}\n")
    

# - Deve ser possível ver uma lista de contatos favoritos
def visualizarContatosFavoritos(is_favorito):
    contatos_quantidades = 0
    for contato in contatos:
        contatos_quantidades += 1
        if contato["favorite"] == is_favorito:
            nome = contato["name"]
            telefone = contato["phone"]
            email = contato["email"]
            favorito = "Sim" if contato["favorite"] == True else "Não"
            print("\nContatos\n")
            print(f"Contato {contatos_quantidades}")
            print(f"Nome: {nome} | Telefone: {telefone}")
            print(f"Email: {email} | Favorito: {favorito}")
            print("----------------------------------------------")

# - Deve ser possível marcar/desmarcar um contato como favorito
def marcarDesmarcarFavorito(idx_contato):
    contato_alterar = contatos[idx_contato-1]
    favorito = False if contato_alterar["favorite"] == True else True
    contato_alterar["favorite"] = favorito
    if favorito == True:
        print(f"Contato {idx_contato} marcado como favorito.\n")
    else:
        print(f"Contato {idx_contato} desmarcado como favorito.\n")
# - Deve ser possível apagar um contato
def deletarContato(idx_contato):
    del contatos[idx_contato-1]
    print(f"Contato {idx_contato} deletado")

# - ADICIONAL: Adicionar contato
def adicionarContato(objeto_contato):
    nome = objeto_contato[0]
    telefone = objeto_contato[1]
    email = objeto_contato[2]
    favorito = objeto_contato[3]
    contato = {
         "name": nome,
         "phone": telefone,
         "email": email,
         "favorite": favorito
     }
    contatos.append(contato)
    print(f"Contato adicionado")

sair = False

while sair == False:
    print("\nGerenciador de contatos")
    print("1 - Visualizar contatos")
    print("2 - Editar contato")
    print("3 - Visualizar contatos favoritos")
    print("4 - Marcar/desmarcar contato como favorito")
    print("5 - Adicionar contato")
    print("6 - Deletar contato")
    print("7 - Sair\n")
    escolha = int(input("Digite a opção: "))

    if escolha == 1:
        visualizarContatos()
    elif escolha == 2:
        visualizarContatos()
        idx_contato = int(input("Digite o índice do contato: "))
        chave_alterar = int(input("Qual chave deseja alterar (1-Nome, 2-Telefone, 3-Email): "))
        valor_alterar = input("Digite o novo valor: ")
        editarContato(idx_contato, chave_alterar, valor_alterar)
    elif escolha == 3:
        is_favorito = True
        visualizarContatosFavoritos(is_favorito)
    elif escolha == 4:
        marcar_desmarcar = input("Marcar ou desmarcar como favorito (M/D): ").lower()
        is_favorito = False if marcar_desmarcar == "m" else True
        visualizarContatosFavoritos(is_favorito)
        idx_contato = int(input("Digite o índice do contato: "))
        marcarDesmarcarFavorito(idx_contato)
    elif escolha == 5:
        nome = input("Digite o nome: ")
        telefone = str(input("Digite o telefone: "))
        email = input("Digite o email: ")
        favorito = input("Marque como favorito (S/N): ").lower()
        favorito = True if favorito == "s" else False
        adicionarContato([nome, telefone, email, favorito])
    elif escolha == 6:
        visualizarContatos()
        idx_contato = int(input("Digite o índice do contato: "))
        deletarContato(idx_contato)
    elif escolha == 7:
        sair = True
        print("Saindo...")   
        
# Como chamar cada função:
#   visualizarContatos()
#   editarContato(index do contato, chave do valor para alterar, valor novo) 
#   visualizarContatosFavoritos(True para favoritos e False para não favoritos)
#   marcarDesmarcarFavorito(index do contato)
#   deletarContato(index do contato)
#   adicionarContato([nome(string), telefone(string), email(string), favorito(booleano)])