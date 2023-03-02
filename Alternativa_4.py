valores = [["SP", 6783643], ["RJ", 3667866], ["MG", 2922988], ["ES", 2716548], ["Outros", 1984953]]

somaValores = 0
for valor in valores: 
    somaValores += valor[1]

for valor in valores:
    print(f"{valor[0]} : {round(((valor[1]*100)/somaValores), 2)}%")
