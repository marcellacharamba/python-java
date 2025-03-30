nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media_simples = (nota1 + nota2 + nota3) / 3

media_ponderada_1 = (nota1 * 2 + nota2 * 2 + nota3 * 3) / (2 + 2 + 3)

media_ponderada_2 = (nota1 * 1 + nota2 * 2 + nota3 * 2) / (1 + 2 + 2)

print(f"\nMédia Aritmética Simples: {media_simples:.2f}")
print(f"Média Ponderada (pesos 2, 2, 3): {media_ponderada_1:.2f}")
print(f"Média Ponderada (pesos 1, 2, 2): {media_ponderada_2:.2f}")
