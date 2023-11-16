from rich.console import Console
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

    for line in header_data.split('\n'):
        data = line.split(': ')
        headers.update({data[0]: data[1]})
        if len(data[1]) <= terminal_size[0]:
            str_headers += f"'{data[0]}': '{data[1]}',\n\t"
        else:
            results = split_string(data[1], terminal_size[0])
            str_headers += f"'{data[0]}': '{results[0]}',\n\t"
            for result in results[1:-1]:
                str_headers += f"'{result}'\n\t"
            str_headers += f"'{results[-1]}',\n\t"
    str_headers += "\n}"
    return headers, str_headers


header_data = header_file('header.txt')
headers, str_headers = str_to_json(header_data)
copy_to_clipboard(str_headers)  # 将处理好的内容粘贴到剪切板
print(str_headers)
