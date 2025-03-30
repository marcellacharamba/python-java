numero = int(input("Digite um número inteiro maior que 1: "))

if numero <= 1:
    print("Por favor, digite um número maior que 1.")
else:
    def eh_primo(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if eh_primo(numero):
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
