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
        print(f"Contato {contatos_quantidades}")
        print(f"Nome: {nome} | Telefone: {telefone}")
        print(f"Email: {email} | Favorito: {favorito}")
        print("----------------------------------------------")

# - Deve ser possível editar um contato
def editarContato(idx_contato, chave_alterar, valor_alterar):
    contato_alterar = contatos[idx_contato-1]
    print(contato_alterar)
    if chave_alterar == 1:
        contato_alterar["name"] = valor_alterar
    elif chave_alterar == 2:
        contato_alterar["phone"] = valor_alterar
    elif chave_alterar == 3:
        contato_alterar["email"] = valor_alterar
    print(contato_alterar)

# - Deve ser possível ver uma lista de contatos favoritos
def visualizarContatosFavoritos(is_favorito):
    contatos_quantidades = 0
    for contato in contatos:
        if contato["favorite"] == is_favorito:
            contatos_quantidades += 1
            nome = contato["name"]
            telefone = contato["phone"]
            email = contato["email"]
            favorito = "Sim" if contato["favorite"] == True else "Não"
            print(f"Contato {contatos_quantidades}")
            print(f"Nome: {nome} | Telefone: {telefone}")
            print(f"Email: {email} | Favorito: {favorito}")
            print("----------------------------------------------")

# - Deve ser possível marcar/desmarcar um contato como favorito
def marcarDesmarcarFavorito(idx_contato):
    contato_alterar = contatos[idx_contato-1]
    favorito = False if contato_alterar["favorite"] == True else True
    contato_alterar["favorite"] = favorito
    print(contato_alterar)

# - Deve ser possível apagar um contato
def deletarContato(idx_contato):
    del contatos[idx_contato-1]

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

# Como chamar cada função:
#   visualizarContatos()
#   editarContato(index do contato, chave do valor para alterar, valor novo) 
#   visualizarContatosFavoritos(True para favoritos e False para não favoritos)
#   marcarDesmarcarFavorito(index do contato)
#   deletarContato(index do contato)
#   adicionarContato([nome(string), telefone(string), email(string), favorito(booleano)])