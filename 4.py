def bild_pyramide(num: int) -> None:
    for i in range(num):
        print(
            ' ' * (num - i - 1),
            '*' * i, 
            '*' * (i - 1), 
            sep=''
        )


if __name__ == '__main__':
    bild_pyramide(13)
