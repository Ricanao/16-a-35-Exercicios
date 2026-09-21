idade = int(input("Idade: "))
 
if idade < 16:
    categoria = "NAO PODE VOTAR"
elif idade <= 17:
    categoria = "VOTO OPCIONAL"
elif idade <= 69:
    categoria = "VOTO OBRIGATORIO"
else:
    categoria = "VOTO OPCIONAL"
 
print("Resultado:", categoria)
 