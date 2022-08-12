while True:
    try:
        string = input()
        asterisco = string.count('*')
        underline = string.count('_')
        while asterisco and underline != 0:
            #Para asterisco
            if asterisco % 2 == 0:
                string = string.replace('*', '<b>')
                asterisco -= 1
            else:
                string = string.replace('*', '</b>')
                asterisco -= 1
            if underline % 2 == 0:
                string = string.replace('_', '<i>')
                underline -= 1
            else:
                string = string.replace('_', '</i>')
                underline -= 1
        print(string)
    except EOFError:
        break
