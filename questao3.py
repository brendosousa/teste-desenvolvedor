#Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne: 
#• O menor valor de faturamento ocorrido em um dia do mês; 
#• O maior valor de faturamento ocorrido em um dia do mês; 
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal. 

import json
from datetime import datetime

# Carrega os dados do arquivo JSON
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)  

#def media_mensal():      

def menor_faturamento_mes(dados):
    menor_faturamento = {'valor': dados[0]['valor'], 'dias': []}
    dias = []
    for dia in dados:
        if dia['valor'] < menor_faturamento['valor']:
            menor_faturamento['valor'] = dia['valor']

    for dia in dados:
        if dia['valor'] == menor_faturamento['valor']:
            menor_faturamento['dias'].append(dia['dia'])

    return menor_faturamento

print(f'O menor faturamento do mês foi: {menor_faturamento_mes(dados)['valor']}')
print(f'O menor faturamento ocorreu nos dias: {menor_faturamento_mes(dados)['dias']}')

def maior_faturamento_mes(dados):
    maior_faturamento = {'valor': dados[0]['valor'], 'dias': []}
    dias = []
    for dia in dados:
        if dia['valor'] > maior_faturamento['valor']:
            maior_faturamento['valor'] = dia['valor']

    for dia in dados:
        if dia['valor'] == maior_faturamento['valor']:
            maior_faturamento['dias'].append(dia['dia'])

    return maior_faturamento

print(f'O maior faturamento do mês foi: {maior_faturamento_mes(dados)['valor']}')
print(f'O maior faturamento ocorreu nos dias: {maior_faturamento_mes(dados)['dias']}')

def media_mensal(dados):
    media = 0
    for dia in dados:
        if dia['valor'] > 0:
            media += dia['valor']
    media = media / len(dados)
    return media

def numero_de_dias_com_faturamento_acima_da_media(dados):
    dias_acima_media = 0
    media = media_mensal(dados)
    for dia in dados:
        if dia['valor'] > media:
            dias_acima_media += 1
    return dias_acima_media

print(f'A quantidade de dias com faturamento acima da média mensal é {numero_de_dias_com_faturamento_acima_da_media(dados)}')
                 