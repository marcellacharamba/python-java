import json

ARQUIVO = "estoque.json"

def carregar_estoque():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []

def salvar_estoque(estoque):
    with open(ARQUIVO, "w") as f:
        json.dump(estoque, f, indent=4)

def adicionar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    estoque = carregar_estoque()
    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    salvar_estoque(estoque)
    print("Produto adicionado com sucesso!")

def listar_produtos():
    estoque = carregar_estoque()
    total = 0
    print("\nProdutos cadastrados:")
    for p in estoque:
        subtotal = p["quantidade"] * p["preco"]
        total += subtotal
        print(f"{p['nome']} - {p['quantidade']} unidades - R${p['preco']:.2f} cada (Subtotal: R${subtotal:.2f})")
    print(f"\nValor total do estoque: R${total:.2f}")

while True:
    print("\n1. Adicionar produto\n2. Listar produtos\n3. Sair")
    op = input("Escolha: ")
    if op == "1":
        adicionar_produto()
    elif op == "2":
        listar_produtos()
    elif op == "3":
        break
    else:
        print("Opção inválida.")
