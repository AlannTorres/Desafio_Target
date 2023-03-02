import json

with open("dados.json") as file:
    vetor = json.load(file)

quantDias = 0
soma = 0
for dia in vetor:
    if (dia["valor"] != 0):
        soma += dia["valor"]
        quantDias += 1
media = soma/quantDias

contDias = 0
listFaturamento = []
for dia in vetor:
    if (dia["valor"] != 0):
        listFaturamento.append(int(dia["valor"]))
    if (dia["valor"] > media):
        contDias += 1
    
print(f"O maior valor de faturamento ocorrido em um dia do mês: {max(listFaturamento)}")
print(f"O menor valor de faturamento ocorrido em um dia do mês: {min(listFaturamento)}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {contDias}")

