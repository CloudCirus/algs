def calculate_sum(number: int) -> int:
    tmp = 0
    while number:
        divider = 10
        res = number % divider
        number = number // divider
        tmp += res
    return tmp


if __name__ == '__main__':
    print(calculate_sum(456))
