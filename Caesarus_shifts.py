# Шифр Цезаря

ru_lang = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
           'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
en_lang = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def is_valid(num):
    if num.isdigit():
        return 'True'
    else:
        return 'False'


def choice_of_language():
    ln = input('Введите язык(ru/en):')
    if ln == 'ru':
         return'ru'
    elif ln == 'en':
        return 'en'
    elif ln != 'ru'  or ln != 'en':
        while ln != 'ru'  and ln != 'en':
            ln = input('Язык набран некорректно, попробуйте снова: ')
        else:
            return ln


def cipher_string(ln):
    if ln == 'ru':
        ln = ru_lang
    else:
        ln = en_lang
    string = input('Введите строку, которую нужно зашифровать/дешифровать: ')
    string = list(string)
    for i in range(len(string)):
        if str(string[i]).islower():
            if string[i] in ln:
                index = ln.index(string[i])
                if index + k > len(ln)-1:
                    string[i] = ln[(index + k) - len(ln)]
                else:
                    string[i] = ln[index + k]
        else:
            string[i] = string[i].lower()
            if string[i] in ln:
                index = ln.index(string[i])
                if index + k >> len(ln)-1:
                    string[i] = ln[(index + k) - len(ln)].upper()
                else:
                    string[i] = ln[index + k].upper()
    string = ''.join(string)
    return string

k = input('Введите желаемый ключ: ')
while is_valid(k) != 'True':
    k = input('Друг, почему ты ввел не цифру?Введи ее здесь:')
k = int(k)
language = choice_of_language()
code = cipher_string(language)
print(code)

