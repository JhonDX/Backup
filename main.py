import os
from datetime import date
import configparser
import shutil
from logging import CRITICAL, ERROR, WARNING, INFO, DEBUG
from logging import critical, error, warning, info, debug
from logging import basicConfig

from tkinter import *

#COPIAR BACKUP
#ENVIAR PARA NUVEM
#MANDAR EMAIL


#USER UPLOAD SUPORTE@GACCBAHIA.ORG.BR


# TIME
d = date.today().day
m = date.today().month
ano = date.today().year

if d and m <= 9:
    dia = str(f'{d:02}')
    mes = str(f'{m:02}')
else:
    pass
YMD = str(f'{dia}-{mes}-{ano}')

# Criação do objeto ConfigParser
configad = configparser.ConfigParser()

# Leitura do arquivo
configad.read('config.ini')
BACKUP = configad['DIR_BACKUP']['BACKUP']

# CRIANDO PASTA DO BACKUP
if os.path.exists(f'{BACKUP}') == False:
    os.mkdir(f'{BACKUP}')
else:
    pass

# CRIANDO PASTA DO ANO
if os.path.exists(f'{BACKUP}/{ano}') == False:
    os.mkdir(f'{BACKUP}/{ano}')
else:
    pass

# CRIANDO PASTA DO MÊS + ANO
if os.path.exists(f'{BACKUP}/{ano}/{mes}-{ano}') == False:
    os.mkdir(f'{BACKUP}/{ano}/{mes}-{ano}')
else:
    pass

# CRIANDO PASTA DO DIA + MÊS + ANO
if os.path.exists(f'{BACKUP}/{ano}/{mes}-{ano}/{dia}-{mes}-{ano}') == False:
    os.mkdir(f'{BACKUP}/{ano}/{mes}-{ano}/{dia}-{mes}-{ano}')
else:
    pass
if os.path.exists(f'{BACKUP}/{ano}/{mes}-{ano}/{dia}-{mes}-{ano}') == False:
    os.mkdir(f'{BACKUP}/{ano}/{mes}-{ano}/{dia}-{mes}-{ano}')
else:
    pass
if os.path.exists(f'{BACKUP}/{ano}/{mes}-{ano}/{dia}-{mes}-{ano}/log') == False:
    os.mkdir(f'{BACKUP}/{ano}/{mes}-{ano}/{dia}-{mes}-{ano}/log')
else:
    pass

DIR_BACKUP_SAVE = f'{BACKUP}/{ano}/{mes}-{ano}/{dia}-{mes}-{ano}/'
DIR_LOG_SAVE = f'{BACKUP}/{ano}/{mes}-{ano}/{dia}-{mes}-{ano}/log/log.txt'

basicConfig(
    level=DEBUG,
    filename=DIR_LOG_SAVE,
    filemode='a',
    format=':%(asctime)s|%(message)s|'
)




# COPIA COM DATA
COUNT = 1
MAX_COUNT = 50  # Defina o valor máximo para COUNT conforme necessário
while COUNT <= MAX_COUNT:
    try:
        DIR_BACKUP = configad['NOME_BACKUP_COM_DATA'][f'DIR_BACKUP_{COUNT}']
        DIR_NOME = configad['NOME_ARQUIVOS_COM_DATA'][f'DIR_BACKUP_{COUNT}']
        EXT = configad['EXT_ARQUIVO_COM_DATA'][f'EXT_{COUNT}']
        SRC = str(f'{DIR_BACKUP}{DIR_NOME}{YMD}{EXT}')
        DST = str(f'{DIR_BACKUP_SAVE}{DIR_NOME}{YMD}{EXT}')
        arquivo = shutil.copyfile(src=SRC, dst=DST)
        debug(f'{arquivo}, O Arquivo foi copiado')

    except KeyError as erro:
        debug(f'Arquivo não encontrado {erro}')
        break

    COUNT += 1




COUNT = 1
MAX_COUNT = 50  # Defina o valor máximo para COUNT conforme necessário
# COPIA DOS BACKUP SEM DATA
while COUNT <= MAX_COUNT:
    try:
        DIR_BACKUP = configad['NOME_BACKUP'][f'DIR_BACKUP_{COUNT}']
        DIR_NOME = configad['NOME_ARQUIVOS'][f'DIR_BACKUP_{COUNT}']
        arquivo = shutil.copyfile(src=DIR_BACKUP, dst=f'{DIR_BACKUP_SAVE}/{DIR_NOME}')
        debug(f'{arquivo}: Arquivo Copiado!')

    except KeyError as erro:
        debug(f'Arquivo não encontrado {erro}')
        break

    COUNT += 1