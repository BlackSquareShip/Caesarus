# Шифр Цезаря

ru_lang = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
           'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
en_lang = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def choice_of_language():
    ln = input('Введите язык(ru/en):')
    while ln != 'ru'  and ln != 'en':
        ln = input('Язык набран некорректно, попробуйте снова: ')
    else:
        if ln == 'ru':
            return ru_lang
        else:
            return en_lang


def cipher_string(ln, string):
    string = list(string)
    for symbol in range(len(string)):
        if str(string[symbol]).islower():
            if string[symbol] in ln:
                index = ln.index(string[symbol])
                if index + k > len(ln)-1:
                    string[symbol] = ln[(index + k) - len(ln)]
                else:
                    string[symbol] = ln[index + k]
        else:
            string[symbol] = string[symbol].lower()
            if string[symbol] in ln:
                index = ln.index(string[symbol])
                if index + k > len(ln)-1:
                    string[symbol] = ln[(index + k) - len(ln)].upper()
                else:
                    string[symbol] = ln[index + k].upper()
    string = ''.join(string)
    return string

def decipher_string(ln, string):
    string = list(string)
    for symbol in range(len(string)):
        if str(string[symbol]).islower():
            if string[symbol] in ln:
                index = ln.index(string[symbol])
                if index - k < 0:
                    string[symbol] = ln[(len(ln))-(k - index)]
                else:
                    string[symbol] = ln[index - k]
        else:
            string[symbol] = string[symbol].lower()
            if string[symbol] in ln:
                index = ln.index(string[symbol])
                if index - k < 0:
                    string[symbol] = ln[(len(ln))-(k - index)].upper()
                else:
                    string[symbol] = ln[index - k].upper()
    string = ''.join(string)
    return string

k = input('Введите желаемый ключ: ')
while not k.isdigit():
    k = input('Друг, почему ты ввел не цифру?Введи ее здесь:')
k = int(k)
language = choice_of_language()
string = input('Введите строку')
what_need_to_do = input('Если необходимо зашифровать, напишите букву з, если необходимо дешифровать, введите д: ')
while what_need_to_do != 'д' and what_need_to_do != 'з':
    what_need_to_do = input('Некорректно указано действие, введите снова(з/д): ')
if what_need_to_do == 'з':
    code = cipher_string(language, string)
else:
    code = decipher_string(language, string)
print(code)

