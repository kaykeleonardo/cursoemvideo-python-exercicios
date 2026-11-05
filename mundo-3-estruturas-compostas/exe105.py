def notas(*nota, sit=False):
    '''-> Função para analisar notas dos alunos
    :param nota: uma ou varias notas dos alunos (aceita varias)
    :param sit: valor opcional, se "True" diz a situação do aluno (bom, razoavel, ruim)
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    lista = nota
    total = len(lista)
    media = sum(lista) / len(lista)
    dic = {}

    for pos , valor in enumerate(lista):
        if pos == 0:
            maior = valor
            menor = valor
        elif maior < valor:
            maior = valor
        elif menor > valor:
            menor = valor

    dic['total'] = total
    dic['maior'] = maior
    dic['menor'] = menor
    dic['media'] = f'{media:.2f}'
    
    if sit == True:
        if media >= 7.0:
            dic['situação'] = 'Boa'
        elif media >= 5.0:
            dic['situação'] = 'Razoavel'
        else:
            dic['situação'] = 'Ruim'

    return dic



resp = notas(1,10,12, sit=True)
print(resp)
help(notas)
