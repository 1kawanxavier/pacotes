import requests

#ESCREVO O SITE E ELE MOSTRA O CODIGO FONTE DA PAGINA
response = requests.get('https://www.agenciatk.com/')
print(response.content)
