import os
import time
import configparser
import shutil

#COPIAR BACKUP
#ENVIAR PARA NUVEM
#MANDAR EMAIL


#USER UPLOAD SUPORTE@GACCBAHIA.ORG.BR
AWS_ACCESS_KEY_ID =
AWS_SECRET_ACCESS_KEY =
region =

time =time.localtime()
dia = time.tm_mday
mes = time.tm_mon
ano = time.tm_year


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


DIR_BACKUP = f'{BACKUP}/{ano}/{mes}-{ano}/{dia}-{mes}-{ano}/'
DIR_MACEIO="//maceio/banco_backup$/teste.txt"

shutil.copyfile(src=DIR_MACEIO, dst=DIR_BACKUP)
