# -*- coding: utf-8 -*-
from rich.console import Console
from time import sleep

console = Console()


def header_file(header_file):
    with open(header_file, 'r', encoding='utf-8') as file:
        header_data = file.read()

    return header_data


def str_to_json(header_data):
    headers = {}
    for line in header_data:
        data = line.split(': ')
        headers.update({data[0]: data[1]})
    return headers


# header_data = input('请输入headers：')
console.rule("[bold blue]请输入headers：")
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
headers = str_to_json(lines)
console.rule("[bold blue]分割线~")
console.print(headers)

print()
# with console.status("[red]Working...[/]"):
for i in range(10, 0, -1): print('\r', f"程序将在{i}秒后自动关闭", end='   ', flush=True), sleep(1)
