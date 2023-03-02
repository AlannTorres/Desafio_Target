palavra = input("Digite uma palavra: ").lower()

newPalavra = ""
cont = 1
for i in range(len(palavra)):
    newPalavra = newPalavra + palavra[-cont]
    cont += 1
print(f"'{palavra}' inversa = '{newPalavra}'")