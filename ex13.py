salario_inicial = float(input("Digite o salário inicial: R$ "))
anos = int(input("Digite o número de anos: "))

aumento_percentual = float(input("Digite o aumento percentual inicial (em %): ")) / 100

salario_atual = salario_inicial

for ano in range(1, anos + 1):
    salario_atual += salario_atual * aumento_percentual
    aumento_percentual *= 2  

print(f"O salário após {anos} anos será: R$ {salario_atual:.2f}")
