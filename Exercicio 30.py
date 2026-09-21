imovel = float(input("Valor do imóvel: "))
salario = float(input("Salário: "))
anos = int(input("Prazo (anos): "))
 
prestacao = imovel / (anos * 12)
limite = salario * 0.30
 
print("Prestação: R$", f"{prestacao:.2f}".replace(".", ","))
print("Limite: R$", f"{limite:.2f}".replace(".", ","))
 
if prestacao <= limite:
    print("Resultado: APROVADO")
else:
    print("Resultado: NEGADO")
 