import json

ARQUIVO = "assentos.json"

def criar_mapa(linhas=5, colunas=5):
    return [["Livre" for _ in range(colunas)] for _ in range(linhas)]

def carregar_assentos():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        mapa = criar_mapa()
        salvar_assentos(mapa)
        return mapa

def salvar_assentos(mapa):
    with open(ARQUIVO, "w") as f:
        json.dump(mapa, f, indent=4)

def mostrar_assentos(mapa):
    print("\nMapa de assentos (L = Livre / R = Reservado):")
    for i, linha in enumerate(mapa):
        print(f"Linha {i+1}: " + " | ".join(["L" if a == "Livre" else "R" for a in linha]))

def reservar_assento():
    mapa = carregar_assentos()
    mostrar_assentos(mapa)
    try:
        linha = int(input("Linha: ")) - 1
        coluna = int(input("Coluna: ")) - 1
        if mapa[linha][coluna] == "Livre":
            mapa[linha][coluna] = "Reservado"
            salvar_assentos(mapa)
            print("Reserva feita com sucesso!")
        else:
            print("Esse assento já está reservado.")
    except:
        print("Entrada inválida.")

def cancelar_reserva():
    mapa = carregar_assentos()
    mostrar_assentos(mapa)
    try:
        linha = int(input("Linha para cancelar: ")) - 1
        coluna = int(input("Coluna: ")) - 1
        if mapa[linha][coluna] == "Reservado":
            mapa[linha][coluna] = "Livre"
            salvar_assentos(mapa)
            print("Reserva cancelada.")
        else:
            print("Esse assento já está livre.")
    except:
        print("Entrada inválida.")

while True:
    print("\n1. Ver mapa de assentos\n2. Reservar assento\n3. Cancelar reserva\n4. Sair")
    op = input("Escolha: ")
    if op == "1":
        mostrar_assentos(carregar_assentos())
    elif op == "2":
        reservar_assento()
    elif op == "3":
        cancelar_reserva()
    elif op == "4":
        break
    else:
        print("Opção inválida.")
