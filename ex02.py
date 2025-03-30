segundos = int(input("Digite um valor em segundos: "))

dias = segundos // 86400  
resto = segundos % 86400

horas = resto // 3600  
resto = resto % 3600

minutos = resto // 60  
segundos_restantes = resto % 60  

print(f"\n{segundos} segundos equivalem a:")
print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
