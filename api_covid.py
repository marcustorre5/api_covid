import requests
import json

print('=' * 13)
print('API COVID')
print('=' * 13)
print(end='\n')

def covid():

    # Link da Api #
    url = 'https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total'

    # País que deseja capturar os dados #
    querystring = {"country":"Brazil"}

    # Credenciais da sua conta da rapid Api #
    # https://rapidapi.com/KishCom/api/covid-19-coronavirus-statistics #
    headers = {
        'x-rapidapi-host': 'covid-19-coronavirus-statistics.p.rapidapi.com',
        'x-rapidapi-key': '6399eeb32bmsh67fc3e3c23cb51dp175bc4jsndd5a51c33dce'
    }

    # GET na Api #
    response = requests.request("GET", url, headers=headers, params=querystring)

    # Trata retorno da Api e mostra os dados #
    dados = json.loads(response.text)
    print(dados,'data')

covid()

print(end='\n')
while True:
    p1 = str(input('Deseja repetir os resultados?\n [S] para sim\n [N] para não\n')).upper()

    if p1 == 'S':
        covid()
    if p1 == 'N':
        exit()

    else:
        exit()

