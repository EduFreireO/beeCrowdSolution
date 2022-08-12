while True:
    try:
        string = list(input())
        maiscula = True
        i = 0
        for letra in string:
            if 65 <= ord(letra) <= 90 or 97 <= ord(letra) <= 122:
                if maiscula:
                    if 97 <= ord(letra) <= 122:
                        string[i] = chr(ord(letra) - 32)
                    maiscula = False
                else:
                    if 65 <= ord(letra) <= 90:
                        string[i] = chr(ord(letra) + 32)
                    maiscula = True
            i += 1
        string = ''.join(string)
        print(string)
    except EOFError:
        break
