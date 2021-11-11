
# Строка которую будет кодировать
message = input("Введите сообщение ")

# ключ смещения
key = int(input("Введите ключ (Смещение) "))

# говорит программу будет кодировать или декодировать
mode = 'encrypt' # установить 'encrypt' или 'decrypt'

# алфавит
LETTERS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'

# переменная для хранения зашифрованной строки
translated = ''

# переводим все буквы в заглавные
message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        # получаем номер символа
        num = LETTERS.find(symbol) # get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key


        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # добавляем зашифрованную букву в переменную
        translated = translated + LETTERS[num]

    else:
        translated = translated + symbol

# Выводим
print("Шифр Цезаря")
print("Исходное сообщение: " + message)
print("Зашифрованное сообщение: " + translated)
