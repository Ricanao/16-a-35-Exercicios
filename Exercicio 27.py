peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
 
imc = peso / (altura * altura)
 
if imc < 18.5:
    classificacao = "ABAIXO DA FAIXA"
elif imc < 25.0:
    classificacao = "FAIXA NORMAL"
elif imc < 30.0:
    classificacao = "ACIMA DA FAIXA"
else:
    classificacao = "FAIXA ELEVADA"
 
print("IMC:", f"{imc:.1f}".replace(".", ","))
print("Classificação:", classificacao)
 