n = int(input("Informe um número: "))

penultimo = 0
ultimo = 1
pertenceOrdem = False
for cont in range(n):
    atual = ultimo + penultimo
    ultimo = atual
    penultimo = ultimo
    if (atual == n or n == 0):
        pertenceOrdem = True
        break

if (pertenceOrdem):
    print("Numero pertence a sequencia!")
else:
    print("Numero não pertence a sequencia!")
