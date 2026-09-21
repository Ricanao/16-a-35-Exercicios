nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2
 
print("Média:", f"{media:.1f}".replace(".", ","))
 
if media >= 7.0:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")
 