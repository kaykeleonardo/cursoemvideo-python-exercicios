from time import sleep


def maior(*num):
    maior = 0
    print("-=" * 30)
    print("Analisando os valores passados...")
    for x in num:
        print(f"{x} ", end="", flush=True)
        sleep(0.4)
        if x > maior:
            maior = x
    print(f"Foram informados {len(num)} valores ao todo")
    print(f"Maior valor digitado foi {maior}")


maior(5, 3, 2, 18, 25, 3, 9, 15)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
