dias = {
    1: "SEGUNDA-FEIRA",
    2: "TERCA-FEIRA",
    3: "QUARTA-FEIRA",
    4: "QUINTA-FEIRA",
    5: "SEXTA-FEIRA",
    6: "SABADO",
    7: "DOMINGO",
}
 
numero = int(input("Número (1-7): "))
print(dias.get(numero, "OPCAO INVALIDA"))
 