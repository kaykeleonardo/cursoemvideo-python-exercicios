def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg:.1f}x{comp:.1f} é de {area:.1f}m²')

print("Controle do Terreno")
print(f"-=" * len('Controle do Terreno'))

largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
area(largura, comprimento)

