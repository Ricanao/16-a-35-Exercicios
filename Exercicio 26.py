salario = float(input("Salário atual: "))
 
if salario <= 1500:
    percentual = 15
elif salario <= 3000:
    percentual = 10
else:
    percentual = 5
 
aumento = salario * percentual / 100
novo_salario = salario + aumento
 
print(f"Percentual: {percentual}%")
print("Aumento: R$", f"{aumento:.2f}".replace(".", ","))
print("Novo salário: R$", f"{novo_salario:.2f}".replace(".", ","))
 