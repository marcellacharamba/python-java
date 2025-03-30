def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = []
numero = 2

while len(primos) < 100:
    if eh_primo(numero):
        primos.append(numero)
    numero += 1

print("Os 100 primeiros números primos:")
print(primos)
