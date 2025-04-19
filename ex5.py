import json

arquivo = "contatos.json"

def carregar():
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except:
        return []

def salvar(contatos):
    with open(arquivo, "w") as f:
        json.dump(contatos, f)

def adicionar():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contatos = carregar()
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    salvar(contatos)

def buscar():
    nome = input("Buscar por nome: ")
    contatos = carregar()
    for c in contatos:
        if nome.lower() in c["nome"].lower():
            print(f"{c['nome']} - {c['telefone']} - {c['email']}")

def menu():
    while True:
        print("\n1. Adicionar contato\n2. Buscar contato\n3. Sair")
        op = input("Escolha: ")
        if op == "1": adicionar()
        elif op == "2": buscar()
        elif op == "3": break

menu()
