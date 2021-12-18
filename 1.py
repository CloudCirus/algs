from typing import Union


def fined_elem(arg: str, target: str) -> Union[str, int]:
    for char in arg:
        if target == char:
            return char
        else:
            return -1


if __name__ == '__main__':
    print(fined_elem('Строка', 'А'))
