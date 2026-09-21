nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2
 
if media < 5.0:
    situacao = "REPROVADO"
elif media < 7.0:
    situacao = "RECUPERACAO"
else:
    situacao = "APROVADO"
 
print("Média:", f"{media:.1f}".replace(".", ","))
print("Situação:", situacao)
 