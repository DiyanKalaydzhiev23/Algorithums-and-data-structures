import re

pattern = r"[tf]\s\?\s\d\s\:\s\d"


def evaluate(line):
    condition = line[0]
    t_arg, f_arg = [el.strip() for el in line[3:].split(':')]
    return t_arg if condition == 't' else f_arg


def func(line: str):
    matches = re.findall(pattern, line)

    for match in matches:
        line = line.replace(match, evaluate(match))

    if '?' in line:
        line = func(line)

    return line


input_line = input()
print(func(input_line))
