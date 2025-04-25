import json

ARQUIVO = "usuarios.json"

def carregar_usuarios():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as f:
        json.dump(usuarios, f, indent=4)

def criar_conta():
    usuarios = carregar_usuarios()
    nome = input("Usuário: ")
    if nome in usuarios:
        print("Usuário já existe.")
        return
    senha = input("Senha: ")
    usuarios[nome] = {"senha": senha, "saldo": 0, "transacoes": []}
    salvar_usuarios(usuarios)
    print("Conta criada com sucesso!")

def login():
    usuarios = carregar_usuarios()
    nome = input("Usuário: ")
    senha = input("Senha: ")
    if nome in usuarios and usuarios[nome]["senha"] == senha:
        print(f"Bem-vindo, {nome}!")
        menu_banco(nome, usuarios)
    else:
        print("Login inválido.")

def menu_banco(nome, usuarios):
    while True:
        print("\n1. Ver saldo\n2. Depositar\n3. Sacar\n4. Ver transações\n5. Sair")
        op = input("Escolha: ")
        if op == "1":
            print(f"Saldo: R${usuarios[nome]['saldo']:.2f}")
        elif op == "2":
            valor = float(input("Valor: "))
            usuarios[nome]["saldo"] += valor
            usuarios[nome]["transacoes"].append(f"Depósito de R${valor:.2f}")
            salvar_usuarios(usuarios)
        elif op == "3":
            valor = float(input("Valor: "))
            if usuarios[nome]["saldo"] >= valor:
                usuarios[nome]["saldo"] -= valor
                usuarios[nome]["transacoes"].append(f"Saque de R${valor:.2f}")
                salvar_usuarios(usuarios)
            else:
                print("Saldo insuficiente.")
        elif op == "4":
            print("Histórico:")
            for t in usuarios[nome]["transacoes"]:
                print("-", t)
        elif op == "5":
            break
        else:
            print("Opção inválida.")

while True:
    print("\n1. Criar conta\n2. Login\n3. Sair")
    op = input("Escolha: ")
    if op == "1":
        criar_conta()
    elif op == "2":
        login()
    elif op == "3":
        break
    else:
        print("Opção inválida.")
