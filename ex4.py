import json

arquivo = "banco.json"

def carregar():
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except:
        return {}

def salvar(usuarios):
    with open(arquivo, "w") as f:
        json.dump(usuarios, f)

def criar():
    nome = input("Usuário: ")
    senha = input("Senha: ")
    usuarios = carregar()
    if nome not in usuarios:
        usuarios[nome] = {"senha": senha, "saldo": 0, "log": []}
        salvar(usuarios)
        print("Conta criada.")
    else:
        print("Usuário já existe.")

def login():
    nome = input("Usuário: ")
    senha = input("Senha: ")
    usuarios = carregar()
    if nome in usuarios and usuarios[nome]["senha"] == senha:
        return nome
    else:
        print("Login inválido.")
        return None

def operacoes(usuario):
    while True:
        print("\n1. Depositar\n2. Sacar\n3. Extrato\n4. Sair")
        op = input("Escolha: ")
        usuarios = carregar()
        if op == "1":
            valor = float(input("Valor: "))
            usuarios[usuario]["saldo"] += valor
            usuarios[usuario]["log"].append(f"+ R${valor}")
        elif op == "2":
            valor = float(input("Valor: "))
            if usuarios[usuario]["saldo"] >= valor:
                usuarios[usuario]["saldo"] -= valor
                usuarios[usuario]["log"].append(f"- R${valor}")
            else:
                print("Saldo insuficiente.")
        elif op == "3":
            print(f"Saldo: R${usuarios[usuario]['saldo']}")
            for item in usuarios[usuario]["log"]:
                print(item)
        elif op == "4":
            break
        salvar(usuarios)

def menu():
    while True:
        print("\n1. Criar conta\n2. Entrar\n3. Sair")
        op = input("Escolha: ")
        if op == "1": criar()
        elif op == "2":
            u = login()
            if u: operacoes(u)
        elif op == "3": break

menu()
