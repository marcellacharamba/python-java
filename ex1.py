import json

arquivo = "tarefas.json"

def carregar():
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except:
        return []

def salvar(tarefas):
    with open(arquivo, "w") as f:
        json.dump(tarefas, f)

def adicionar():
    desc = input("Descrição: ")
    prazo = input("Prazo (AAAA-MM-DD): ")
    tarefas = carregar()
    tarefas.append({"descricao": desc, "prazo": prazo, "concluida": False})
    salvar(tarefas)

def listar():
    tarefas = carregar()
    tarefas.sort(key=lambda x: x["prazo"])
    for i, t in enumerate(tarefas):
        status = "✔️" if t["concluida"] else "❌"
        print(f"{i+1}. {t['descricao']} - {t['prazo']} - {status}")

def concluir():
    listar()
    n = int(input("Número da tarefa: ")) - 1
    tarefas = carregar()
    if 0 <= n < len(tarefas):
        tarefas[n]["concluida"] = True
        salvar(tarefas)

def menu():
    while True:
        print("\n1. Adicionar\n2. Listar\n3. Concluir\n4. Sair")
        op = input("Escolha: ")
        if op == "1": adicionar()
        elif op == "2": listar()
        elif op == "3": concluir()
        elif op == "4": break

menu()
