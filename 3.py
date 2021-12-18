def calculate_sum(number: int) -> int:
    res = 0
    while number:
        one = number % 10
        number = number // 10
        res += one
    return res


if __name__ == '__main__':
    print(calculate_sum(456))
