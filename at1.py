import json
from datetime import datetime

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa():
    descricao = input("Descrição: ")
    prazo = input("Prazo (AAAA-MM-DD): ")
    tarefas = carregar_tarefas()
    tarefas.append({"descricao": descricao, "prazo": prazo, "concluida": False})
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    tarefas = sorted(carregar_tarefas(), key=lambda x: x["prazo"])
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for i, t in enumerate(tarefas):
        status = "Concluída" if t["concluida"] else "Pendente"
        print(f"{i+1}. {t['descricao']} - até {t['prazo']} ({status})")

def marcar_concluida():
    listar_tarefas()
    try:
        i = int(input("Número da tarefa concluída: ")) - 1
        tarefas = carregar_tarefas()
        tarefas[i]["concluida"] = True
        salvar_tarefas(tarefas)
        print("Tarefa marcada como concluída!")
    except:
        print("Entrada inválida.")

# Menu
while True:
    print("\n1. Adicionar tarefa\n2. Listar tarefas\n3. Marcar como concluída\n4. Sair")
    op = input("Escolha: ")
    if op == "1":
        adicionar_tarefa()
    elif op == "2":
        listar_tarefas()
    elif op == "3":
        marcar_concluida()
    elif op == "4":
        break
    else:
        print("Opção inválida.")

