import requests
import json

dicionario_cartas = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': '10',
    'AS': 'ACE',
    'DAMA': 'QUEEN',
    'VALETE': 'JACK',
    'REI': 'KING',
    'QUEEN': 'DAMA',
    'JACK': 'VALETE',
    'KING': 'REI',
    'ACE': 'AS',

}
dicionario_naipes = {
    'COPAS': 'HEARTS',
    'PAUS': 'CLUBS',
    'ESPADAS': 'SPADES',
    'OUROS': 'DIAMONDS',
    'HEARTS': 'COPAS',
    'CLUBS': 'PAUS',
    'SPADES': 'ESPADAS',
    'DIAMONDS': 'OUROS'

}

valor = input('Infome o valor da carta: ').upper()
naipe = input('Informe o naípe: ').upper()

response_baralho = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')

baralho = response_baralho.json()
deck_id = baralho['deck_id']

while True:

    response_carta = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1')
    carta = response_carta.json()['cards'][0]
    cartas_no_baralho = response_carta.json()['remaining']

    if carta['value'] == dicionario_cartas[valor] and carta['suit'] == dicionario_naipes[naipe]:
        print('\nEncontrei sua carta!!')
        print('Para consultar a carta encontrada, copie o link dentro do json criado e cole no seu navegador!')

        with open('carta.json()', 'w') as arquivo_carta:
            json.dump(carta, arquivo_carta)

        break

    else:
        valor_comprado = dicionario_cartas[carta['value']]
        naipe_comprado = dicionario_naipes[carta['suit']]
        print(f'Carta comprada: {valor_comprado} de {naipe_comprado} está incorreta!\n')
        print(f'Ainda restam {cartas_no_baralho} cartas no baralho\n')
