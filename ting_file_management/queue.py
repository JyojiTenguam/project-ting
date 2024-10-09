from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if len(self._data) == 0:
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self._data == []
