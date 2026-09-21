numero = int(input("Digite um número: "))
 
div3 = numero % 3 == 0
div5 = numero % 5 == 0
 
if div3 and div5:
    print("Resultado: DIVISIVEL POR 3 E 5")
elif div3:
    print("Resultado: DIVISIVEL APENAS POR 3")
elif div5:
    print("Resultado: DIVISIVEL APENAS POR 5")
else:
    print("Resultado: NAO DIVISIVEL POR 3 NEM 5")
 