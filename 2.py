def fined_index(array: list, target: str) -> str:
    try: 
        return array.index(target)
    except:
        return 'ooops'


if __name__ == '__main__':
    array = ['lol', 'lollol', 'ololo']
    print(fined_index(array, 'lol'))
