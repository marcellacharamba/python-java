num_impar = int(input("Digite um número ímpar: "))

if num_impar % 2 == 0:
    print("Por favor, digite um número ímpar.")
else:
    num_anterior = num_impar - 2
    num_proximo = num_impar + 2

    diferenca = (num_proximo ** 2) - (num_anterior ** 2)

    print(f"A diferença entre o quadrado do próximo número ímpar ({num_proximo ** 2}) e do número anterior ({num_anterior ** 2}) é: {diferenca}")
