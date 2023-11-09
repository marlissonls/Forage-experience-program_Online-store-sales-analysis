import urllib.request
from os.path import dirname

MAIN_PROJECT_PATH = dirname(dirname(__file__))

# File URL
url = 'https://cdn.theforage.com/vinternships/companyassets/ifobHAoMjQs9s6bKS/5XsFFJu2oCLdmYJW2/1654309626143/Online%20Retail%20Data%20Set.xlsx'

# Downloaded file path
file_name = 'raw_' + url.split('/')[-1].replace('%20','_').lower()
file_path = f'{MAIN_PROJECT_PATH}/data_source/raw_data/{file_name}'

# Download file
urllib.request.urlretrieve(url, file_path)

print(f'File "{file_name}" downloaded!')
