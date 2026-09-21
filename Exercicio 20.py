a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
 
valores = sorted([a, b, c])
print("Ordem crescente:", ", ".join(str(v) for v in valores))
 