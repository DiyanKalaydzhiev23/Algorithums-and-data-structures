import re


pattern = r"[tf]\s\?\s\d\s\:\s\d"


def create_result(expression):
    true, false = [x.strip() for x in expression[3:].split(':')]
    statement = expression[0]

    return true if statement == 't' else false


def find_all(expression):
    result = re.findall(pattern, expression)

    for r in result:
        expression = expression.replace(r, create_result(r))

    if '?' in expression:
        expression = find_all(expression)

    return expression


print(find_all(input()))
