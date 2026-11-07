from datetime import date


def voto(anoNasc):
    idade = date.today().year - anoNasc
    if 16 <= idade < 18 or idade >= 70:
        return f"Com {idade} anos: Voto Opcional"
    elif idade >= 18:
        return f"Com {idade} anos: Voto Obrigatorio"
    else:
        return f"Com {idade} anos: Voto Proibido"


print("-" * 30)
nasc = int(input("Digite o ano de Nascimento: "))
print(voto(nasc))