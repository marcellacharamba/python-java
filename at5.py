import json

ARQUIVO = "contatos.json"

def carregar_contatos():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []

def salvar_contatos(contatos):
    with open(ARQUIVO, "w") as f:
        json.dump(contatos, f, indent=4)

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contatos = carregar_contatos()
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    salvar_contatos(contatos)
    print("Contato adicionado!")

def buscar_contato():
    nome = input("Nome para buscar: ")
    contatos = carregar_contatos()
    encontrados = [c for c in contatos if nome.lower() in c["nome"].lower()]
    if encontrados:
        for c in encontrados:
            print(f"{c['nome']} - Tel: {c['telefone']} - Email: {c['email']}")
    else:
        print("Nenhum contato encontrado.")


while True:
    print("\n1. Adicionar contato\n2. Buscar contato\n3. Sair")
    op = input("Escolha: ")
    if op == "1":
        adicionar_contato()
    elif op == "2":
        buscar_contato()
    elif op == "3":
        break
    else:
        print("Opção inválida.")
