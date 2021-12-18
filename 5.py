from datetime import datetime
import random


def count_runtime(func):
    def inner(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return inner


@count_runtime
def stupid_sort(seq: list) -> list:
    i, size = 1, len(seq)
    while size > i:
        if seq[i - 1] > seq[i]:
            seq[i - 1], seq[i] = seq[i], seq[i - 1]
            i = 1
        else:
            i += 1
    return seq


@count_runtime
def bubble_sort(seq: list) -> list:
    changer = True
    while changer:
        changer = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                changer = True
    return seq


if __name__ == '__main__':
    array = [random.randint(0, 9) for _ in range(100)]
    print(stupid_sort(array))
    print(bubble_sort(array))
