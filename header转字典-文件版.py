from rich.console import Console

console = Console()


def header_file(header_file):
    with open(header_file, 'r', encoding='utf-8') as file:
        header_data = file.read()

    return header_data


def str_to_json(header_data):
    headers = {}
    for line in header_data.split('\n'):
        data = line.split(': ')
        headers.update({data[0]: data[1]})
    return headers


header_data = header_file('header.txt')
headers = str_to_json(header_data)

console.print(headers)