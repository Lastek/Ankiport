import ast
import os
import sys


def open_file(filename: str) -> list:
    contents: list = []
    with open(filename, "r") as file:
        contents.extend(file.readlines())
    return contents


def write_file(filename: str, data: list[str]):
    with open(filename, "w") as file:
        file.writelines(data)


def strip_strings(contents: list) -> list:
    formatted = []
    for x in contents:
        x: str
        x.strip()
        x = x.strip('\n')
        if x != '':
            formatted.append(x)
    return formatted


def load_tags(tags_file):
    """Load keyword-to-tag mapping from a file."""
    with open(tags_file, 'r', encoding='utf-8') as f:
        return ast.literal_eval(f.read().strip())


def generate_tags(answer, keywords_to_tags):
    """Analyze the answer text and generate tags."""
    tags = set()
    for keyword, tag in keywords_to_tags.items():
        if keyword.lower() in answer.lower():
            tags.add(tag)
    return " ".join(sorted(tags))

def check_ext(string:str) -> str|int:
    if string.endswith('.txt'):
        input_file = string
    elif string.find('.') != -1:
        print("File extension must be '.txt'")
        sys.exit(-1)
    else:
        input_file = string + '.txt'
    return input_file

def processor_html_tags(data):
    pass

def generate_anki_file(filename:str, tagfilename:str):

    input_file = check_ext(filename)
    contents = open_file(input_file)
    
    tag_file = check_ext(tagfilename)
    keywords_to_tags = load_tags(tag_file)

    formatted = strip_strings(contents)

    full: list = []
    stack: list = []
    stack_begin: bool = True
    for x in formatted:
        x: str
        if (x.casefold().startswith('card') and stack_begin == False):
            stack_begin = True
            full.append(stack.copy())
            stack = []

        stack.append(x.strip())
        stack_begin = False

    output: list = []
    for x in full:
        c: str = f'{x[1]}\t'
        for y in x[2:]:
            c += f'{y}<br>'
        tags = generate_tags(c, keywords_to_tags)
        c += f'\t{tags}\n'
        output.append(c)

    input_file_name_no_ext = input_file.removesuffix('.txt')
    write_file(f'{input_file_name_no_ext}_anki.txt', output)


if __name__ == '__main__':

    print("Current working directory:", os.getcwd())

    # Load JSON data from the file
    if len(sys.argv) != 3:
        print("Args: file.txt tags.txt")
        sys.exit(1)

    print("Generating file") 
    generate_anki_file(sys.argv[1], sys.argv[2])