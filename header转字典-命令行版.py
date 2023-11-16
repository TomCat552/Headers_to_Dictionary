# -*- coding: utf-8 -*-
from rich.console import Console
from time import sleep
import shutil
import pyperclip

console = Console()


def copy_to_clipboard(text):
    """
    将指定文本复制到剪贴板。

    参数：
    - text (str): 要复制到剪贴板的文本。
    """
    pyperclip.copy(text)


def get_terminal_size():
    """
    获取命令提示符输出窗口的大小。

    返回：
    - Tuple[int, int]: 包含窗口宽度和高度的元组。
    """
    size = shutil.get_terminal_size()
    return size.columns, size.lines


def header_file(header_file):
    with open(header_file, 'r', encoding='utf-8') as file:
        header_data = file.read()

    return header_data


def split_string(input_string, chunk_length):
    """
    将字符串按指定长度分割。

    参数：
    - input_string (str): 要分割的输入字符串。
    - chunk_length (int): 每个分割块的长度。

    返回：
    - List[str]: 包含分割块的列表。
    """
    return [input_string[i:i + chunk_length] for i in range(0, len(input_string), chunk_length)]


def str_to_json(header_data):
    """
    如果请求头内某些字段长度过长导致输出字典换行，粘贴后需要手动处理，为解决此问题使用str_headers自动调整格式
    :param header_data:
    :return:
    """
    headers = {}
    str_headers = ""
    str_headers += "{\n\t"
    # 获取窗口大小，来调整输出宽度
    terminal_size = get_terminal_size()

    for line in header_data:
        data = line.split(': ')
        headers.update({data[0]: data[1]})
        if len(data[1]) <= terminal_size[0] * 0.75:
            str_headers += f"'{data[0]}': '{data[1]}',\n\t"
        else:
            results = split_string(data[1], int(terminal_size[0] * 0.75))
            str_headers += f"'{data[0]}': '{results[0]}'\n\t"
            for result in results[1:-1]:
                str_headers += f"'{result}'\n\t"
            str_headers += f"'{results[-1]}',\n\t"
    str_headers += "}"
    return headers, str_headers


if __name__ == '__main__':
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
    copy_to_clipboard(headers[1])  # 将处理好的内容粘贴到剪切板
    console.rule("[bold blue]分割线~")
    console.print(headers[1])

    print()
    # with console.status("[red]Working...[/]"):
    for i in range(10, 0, -1): print('\r', f"内容已复制,程序将在{i}秒后自动关闭", end='   ', flush=True), sleep(1)
