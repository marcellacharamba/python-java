import json

arquivo = "estoque.json"

def carregar():
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except:
        return []

def salvar(estoque):
    with open(arquivo, "w") as f:
        json.dump(estoque, f)

def adicionar():
    nome = input("Nome do produto: ")
    qtd = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    estoque = carregar()
    estoque.append({"nome": nome, "quantidade": qtd, "preco": preco})
    salvar(estoque)

def listar():
    estoque = carregar()
    total = 0
    for p in estoque:
        print(f"{p['nome']} - Qtd: {p['quantidade']} - R${p['preco']}")
        total += p['quantidade'] * p['preco']
    print(f"Total do estoque: R${total:.2f}")

def menu():
    while True:
        print("\n1. Adicionar\n2. Listar\n3. Sair")
        op = input("Escolha: ")
        if op == "1": adicionar()
        elif op == "2": listar()
        elif op == "3": break

menu()
