mes = int(input("Mês: "))
ano = int(input("Ano: "))
 
if mes in (1, 3, 5, 7, 8, 10, 12):
    print("31 dias")
elif mes in (4, 6, 9, 11):
    print("30 dias")
elif mes == 2:
    bissexto = ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)
    print("29 dias" if bissexto else "28 dias")
else:
    print("MES INVALIDO")
 