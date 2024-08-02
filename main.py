import os
from datetime import date
import configparser
import shutil

#COPIAR BACKUP
#ENVIAR PARA NUVEM
#MANDAR EMAIL


#USER UPLOAD SUPORTE@GACCBAHIA.ORG.BR


#TIME
d = date.today().day
m = date.today().month
ano = date.today().year

if d and m <=9:
    dia =str(f'{d:02}')
    mes = str(f'{m:02}')
else:
    pass
YMD =str(f'{dia}-{mes}-{ano}')


# Criação do objeto ConfigParser
configad = configparser.ConfigParser()

# Leitura do arquivo
configad.read('config.ini')
BACKUP = configad['DIR_BACKUP']['BACKUP']


#CRIANDO PASTA DO BACKUP
if os.path.exists(f'{BACKUP}') == False:
    os.mkdir(f'{BACKUP}')
else:
    pass

#CRIANDO PASTA DO ANO
if os.path.exists(f'{BACKUP}/{ano}') == False:
    os.mkdir(f'{BACKUP}/{ano}')
else:
    pass

#CRIANDO PASTA DO MÊS + ANO
if os.path.exists(f'{BACKUP}/{ano}/{mes}-{ano}') == False:
    os.mkdir(f'{BACKUP}/{ano}/{mes}-{ano}')
else:
    pass

#CRIANDO PASTA DO DIA + MÊS + ANO
if os.path.exists(f'{BACKUP}/{ano}/{mes}-{ano}/{dia}-{mes}-{ano}') == False:
    os.mkdir(f'{BACKUP}/{ano}/{mes}-{ano}/{dia}-{mes}-{ano}')
else:
    pass


DIR_BACKUP_SAVE = f'{BACKUP}/{ano}/{mes}-{ano}/{dia}-{mes}-{ano}/'


#COPIA COM DATA
COUNT = 1
MAX_COUNT = 50 # Defina o valor máximo para COUNT conforme necessário

while COUNT <= MAX_COUNT:
    try:
        DIR_BACKUP = configad['NOME_BACKUP_COM_DATA'][f'DIR_BACKUP_{COUNT}']
        DIR_NOME = configad['NOME_ARQUIVOS_COM_DATA'][f'DIR_BACKUP_{COUNT}']
        EXT = configad['EXT_ARQUIVO_COM_DATA'][f'EXT_{COUNT}']
        SRC = str(f'{DIR_BACKUP}{DIR_NOME}{YMD}{EXT}')
        DST = str(f'{DIR_BACKUP_SAVE}{DIR_NOME}{YMD}{EXT}')
        arquivo = shutil.copyfile(src=SRC,dst=DST)
        print(f'Copiando Arquivo!: {arquivo}')

    except KeyError as erro:
        # Se uma das chaves principais não for encontrada, trata-se o erro
        print(f"Chave não encontrada: {erro}")
        # Dependendo do comportamento desejado, você pode decidir se deve continuar ou não
        break  # Saímos do loop externo se uma chave não for encontrada

    COUNT += 1

COUNT = 1
MAX_COUNT = 50 # Defina o valor máximo para COUNT conforme necessário



#COPIA DOS BACKUP SEM DATA
while COUNT <= MAX_COUNT:
    try:
        DIR_BACKUP = configad['NOME_BACKUP'][f'DIR_BACKUP_{COUNT}']
        DIR_NOME = configad['NOME_ARQUIVOS'][f'DIR_BACKUP_{COUNT}']
        # Faça algo com DIR_LOCAL e DIR_BACKUP
        arquivo = shutil.copyfile(src=DIR_BACKUP,dst=f'{DIR_BACKUP_SAVE}/{DIR_NOME}')
        print(f'Copiando Arquivo!: {arquivo}')


    except KeyError as erro:
        # Se a chave não existir no dicionário, trate o erro
        print(f"Chave não encontrada: {erro}")
        break  # Sai do loop se uma chave não for encontrada

    COUNT += 1






