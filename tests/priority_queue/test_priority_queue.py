import pytest
from ting_file_management.priority_queue import PriorityQueue


def create_mock(file_name: str, lines: int):
    return {
        "nome_do_arquivo": file_name,
        "qtd_linhas": lines,
        "linhas_do_arquivo": [file_name] * lines,
    }


def test_basic_priority_queueing():
    queue = PriorityQueue()

    items = [
        ["texto_01.txt", 2],  # Alta prioridade (2 linhas)
        ["texto_02.txt", 8],  # Baixa prioridade (8 linhas)
        ["texto_03.txt", 3],  # Alta prioridade (3 linhas)
        ["texto_04.txt", 1],  # Alta prioridade (1 linha)
        ["texto_05.txt", 6],  # Baixa prioridade (6 linhas)
    ]

    ordered_items = [
        "texto_01.txt",  # 1 linha
        "texto_03.txt",  # 2 linhas
        "texto_04.txt",  # 3 linhas
        "texto_02.txt",  # 6 linhas
        "texto_05.txt",  # 8 linhas
    ]

    for item in items:
        queue.enqueue(create_mock(item[0], item[1]))

    assert len(queue) == 5  # Verifica o tamanho da fila

    # Verifica a ordem de prioridade
    for i in range(len(ordered_items)):
        assert queue.search(i)["nome_do_arquivo"] == ordered_items[i]

    # Adiciona um novo arquivo e verifica sua posição
    new_element = create_mock("texto_06.txt", 7)  # Baixa prioridade
    queue.enqueue(new_element)

    assert len(queue) == 6
    assert queue.search(5)["nome_do_arquivo"] == "texto_06.txt"

    # Remove o elemento com maior prioridade (texto_01.txt)
    removed_element = queue.dequeue()

    assert removed_element is not None
    assert removed_element["nome_do_arquivo"] == "texto_01.txt"
    assert len(queue) == 5

    # Insere um novo arquivo com prioridade alta e verifica sua posição
    new_element = create_mock("texto_07.txt", 2)  # Alta prioridade
    queue.enqueue(new_element)

    # Atualizar a ordem esperada após a inserção do novo elemento
    expected_order_after_enqueue = [
        "texto_03.txt",  # 2 linhas
        "texto_04.txt",  # 3 linhas
        "texto_07.txt",  # 6 linhas
        "texto_02.txt",  # 7 linhas
        "texto_05.txt",  # 8 linhas
    ]

    for i in range(len(expected_order_after_enqueue)):
        assert queue.search(i)
        ["nome_do_arquivo"] == expected_order_after_enqueue[i]

    # Verifica a exceção de índice inválido
    with pytest.raises(IndexError):
        queue.search(8)
