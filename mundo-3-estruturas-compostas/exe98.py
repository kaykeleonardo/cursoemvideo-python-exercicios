from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = passo * -1
    print("-=" * 40)
    print(f"Contando de {inicio} até {fim} de {passo} em {passo}:")
    if inicio < fim:
        while inicio <= fim:
            print(f"{inicio} ", end="", flush=True)
            inicio += passo
            sleep(0.2)
        print("Fim")
    else:
        while inicio >= fim:
            print(f"{inicio} ", end="", flush=True)
            inicio -= passo
            sleep(0.2)
        print("FIM")


contador(10, 100, 8)
contador(10, 1, 1)
print("-=" * 40)
print("Agora é sua vez !")
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)
