preco = float(input("Preço: "))
opcao = int(input("Opção: "))
 
if opcao == 1:
    valor_final = preco * 0.90
elif opcao == 2:
    valor_final = preco * 0.95
elif opcao == 3:
    valor_final = preco
elif opcao == 4:
    valor_final = preco * 1.08
else:
    valor_final = None
 
if valor_final is None:
    print("Opção inválida")
else:
    print("Valor final: R$", f"{valor_final:.2f}".replace(".", ","))
 