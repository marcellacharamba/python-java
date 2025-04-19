import json

arquivo = "assentos.json"

def carregar():
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except:
        return {f"A{i}": False for i in range(1, 11)}

def salvar(mapa):
    with open(arquivo, "w") as f:
        json.dump(mapa, f)

def mostrar():
    mapa = carregar()
    for assento, ocupado in mapa.items():
        status = "🟥" if ocupado else "🟩"
        print(f"{assento}: {status}")

def reservar():
    mapa = carregar()
    assento = input("Assento (ex: A3): ")
    if assento in mapa and not mapa[assento]:
        mapa[assento] = True
        salvar(mapa)
        print("Reserva feita.")
    else:
        print("Assento inválido ou ocupado.")

def cancelar():
    mapa = carregar()
    assento = input("Assento (ex: A3): ")
    if assento in mapa and mapa[assento]:
        mapa[assento] = False
        salvar(mapa)
        print("Reserva cancelada.")
    else:
        print("Assento inválido ou já livre.")

def menu():
    while True:
        print("\n1. Mostrar mapa\n2. Reservar\n3. Cancelar\n4. Sair")
        op = input("Escolha: ")
        if op == "1": mostrar()
        elif op == "2": reservar()
        elif op == "3": cancelar()
        elif op == "4": break

menu()
