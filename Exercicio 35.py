preco_cheio = 30.00
 
idade = int(input("Idade: "))
estudante = input("Estudante (SIM/NAO): ").strip().upper()
 
tem_meia = idade < 12 or estudante == "SIM" or idade >= 60
 
valor = preco_cheio * 0.5 if tem_meia else preco_cheio
 
print("Valor do ingresso: R$", f"{valor:.2f}".replace(".", ","))
 