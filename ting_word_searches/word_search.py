def exists_word(word, instance):
    word_lower = word.lower()
    results = []

    for index in range(len(instance)):
        file_data = instance.search(index)
        file_name = file_data["nome_do_arquivo"]
        occurrences = []
        file_content = open(file_name, 'r').readlines()

        for line_number, line in enumerate(file_content, start=1):
            if word_lower in line.lower():
                occurrences.append({"linha": line_number})
        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })

    return results


def search_by_word(word, instance):
    word_lower = word.lower()
    results = []

    for index in range(len(instance)):
        file_data = instance.search(index)
        file_name = file_data["nome_do_arquivo"]
        occurrences = []
        file_content = open(file_name, 'r').readlines()
        for line_number, line in enumerate(file_content, start=1):
            if word_lower in line.lower():
                occurrences.append({
                    "linha": line_number,
                    "conteudo": line.strip()
                })
        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })

    return results
