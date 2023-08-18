renda = float(input("Digite o valor da renda: "))

if renda <= 2112.00:
    imposto = 0

elif renda <= 2826.65:
    imposto = renda * 0.075

elif renda <= 3751.05:
    imposto = renda * 0.15

elif renda <= 4664.68:
    imposto = renda * 0.225

else:
    imposto = renda * 0.275

r_liquido = renda - imposto

print(f"O valor do Imposto de Renda é: {imposto:.2f}")
print(f"Sua renda Liquida é: {r_liquido:.2f}")