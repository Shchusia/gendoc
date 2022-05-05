def strip_rows(doc_string: str):
    lines = doc_string.expandtabs().splitlines()
    data = [line.strip() for line in lines]
    data = list(filter(lambda x: x, data))
    return "\n".join(data)
