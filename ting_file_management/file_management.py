import sys
import os


def txt_importer(path_file):
    if not os.path.exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return

    if not path_file.endswith('.txt'):
        print("Formato inválido", file=sys.stderr)
        return

    try:
        with open(path_file, 'r') as file:
            lines = file.read().split('\n')
        return lines
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}", file=sys.stderr)
