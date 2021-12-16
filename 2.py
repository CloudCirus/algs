def finedindex(array: list, target: str):
    try: 
        return array.index(target)
    except:
        return 'ooops'


if __name__ == '__main__':
    array = ['lol', 'lollol', 'ololo']
    print(finedindex(array, 'lol'))
