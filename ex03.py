valor_total = float(input("Digite o valor total das mercadorias compradas: R$ "))

if valor_total > 500:
    valor_excedente = valor_total - 500
    imposto = valor_excedente * 0.50
else:
    imposto = 0

print(f"\nValor total da compra: R$ {valor_total:.2f}")
print(f"Imposto a pagar: R$ {imposto:.2f}")
