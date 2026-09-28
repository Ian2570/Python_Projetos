import os
import shutil
from pathlib import Path
from zipfile import ZipFile

#Caminhos

CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'compactando_diretorio_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'arquivo_compactado_zip'
CAMINHO_DESCOMPACTO = CAMINHO_RAIZ / 'arquivo_descompactado'

shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTO, ignore_errors=True)

#Cria o diretório

CAMINHO_ZIP_DIR.mkdir(exist_ok=True)

def criar_arquivo(qtd:int, zip_dir:Path):
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / 'f{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)

criar_arquivo(10, CAMINHO_ZIP_DIR)

#Criando um ZIP e adcionando arquivos.
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            zip.write(os.path.join(root, file), file)

# Lendo arquivos de um zip.
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Extraindo arquivos de um zip.
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)