from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in instance._data:
        if item["nome_do_arquivo"] == path_file:
            return

    lines = txt_importer(path_file)

    if lines is not None:
        file_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines,
        }

        instance.enqueue(file_data)
        print(file_data)


def remove(instance):
    if instance.is_empty():
        print("Não há elementos")
    else:
        file_data = instance.dequeue()
        path_file = file_data["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        file_data = instance.search(position)
        print(file_data)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
