import urllib.request
import os
from os.path import dirname

MAIN = dirname(dirname(__file__))

# URL do arquivo que você deseja baixar
url = 'https://cdn.theforage.com/vinternships/companyassets/ifobHAoMjQs9s6bKS/5XsFFJu2oCLdmYJW2/1654309626143/Online%20Retail%20Data%20Set.xlsx'

# Nome do arquivo de destino
file_name = 'raw_' + url.split('/')[-1].replace('%20','_').lower()

# Pasta de destino para salvar o arquivo baixado
file_path = f'{MAIN}/data_source/raw_data/{file_name}'


# Baixar o arquivo
urllib.request.urlretrieve(url, file_path)

print(f'Arquivo {file_name} baixado!')
