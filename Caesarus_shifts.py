# Шифр Цезаря

en_lang = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipher_string(ln, string):
    word = string.split()

    chip = ''
    for i in word:
        for symbol in range(len(i)):
            i = list(i) 
            count = 0
            for j in i:
                if not j.isalpha():
                    count += 1
            if i[symbol].islower():
                if i[symbol] in ln:
                    index = ln.index(i[symbol])
                    if index + len(i) - count > len(ln)-1:
                        i[symbol] = ln[(index + len(i)-count) - len(ln)]
                    else:
                        i[symbol] = ln[index + len(i)-count]
            else:
                i[symbol] = i[symbol].lower()
                if i[symbol] in ln:
                    index = ln.index(i[symbol])
                    if index + len(i) - count > len(ln)-1:
                        i[symbol] = ln[(index + len(i)-count) - len(ln)].upper()
                    else:
                        i[symbol] = ln[index + len(i)-count].upper()
        i = ''.join(i) 
        chip += i + ' '
    return chip


string = input('Введите строку')
language = en_lang
code = cipher_string(language, string)
print(code)
