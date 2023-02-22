# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contador_acertos = 0

for dic in perguntas:
    print(f"Pergunta: {dic['Pergunta']}\n")
    print('Opções:')

    opcoes = dic['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    escolha = input('Escolha uma opção: ')

    escolha_int = None
    acertou = False
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == dic['Resposta']:
                acertou = True

    print()
    if acertou:
        contador_acertos += 1
        print('PARABÉNS!!! Você acertou!')
    else:
        print('ERRADO!')

    print()

print('Você acertou', contador_acertos)
print('de', len(perguntas), 'perguntas.')
