dias = int(input("Quantos dias o carro foi alugado? "))
km_rodados = float(input("Quantos quilômetros foram percorridos? "))

custo_diario = 90
limite_km = 100
taxa_extra_km = 12

custo_total = dias * custo_diario

if km_rodados > limite_km:
    km_excedente = km_rodados - limite_km
    custo_total += km_excedente * taxa_extra_km

print(f"\nValor total a pagar: R$ {custo_total:.2f}")
