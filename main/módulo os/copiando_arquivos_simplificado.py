import os 
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'DOCUMENTAÇÃO SERVIÇO - Copia')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)