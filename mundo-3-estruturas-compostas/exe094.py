dados = []
soma = 0.0
sexo = True
while True:
    pessoas = {}
    pessoas["Nome"] = input("Nome: ")

    while True:
        pessoas["Sexo"] = input("Sexo: [M/F] ").upper()[0]
        if pessoas["Sexo"] in "MF":
            break
        print("Sexo inválido. Tente Novamente...")

    pessoas["Idade"] = int(input("Idade: "))
    soma += pessoas["Idade"]
    dados.append(pessoas)

    while True:
        parada = input("Quer continuar? [S/N] ").upper()[0]
        if parada in "SN":
            break
        print("ERRO! Digite apenas [S/N]")
    if parada == "N":
        break

print("-=" * 30)
qtd_pessoas = len(dados)
print(f"A) A quantidade de pessoas cadastradas é: {qtd_pessoas}")


media = soma / qtd_pessoas
print(f"B) A media de idade é de {media:.2f} anos")

print("C) Mulheres Adicionadas: ", end=" ")
for x in dados:
    if x["Sexo"] == "F":
        print(f'{x["Nome"]}', end="")

print()
print(f"D) Pessoas com idade acima da média: ", end="")
for x in dados:
    if x["Idade"] > media:
        print("    ")
        for k, v in x.items():
            print(f"{k} = {v}; ", end="")
        print()
print("-=" * 30)
