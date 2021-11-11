def encrypt(text, gamma):
    textLen = len(text)
    gammaLen = len(gamma)
    alphabeth = 'abcdefghijklmnopqrstuvwxyz'
    #Формируем ключевое слово(растягиваем гамму на длину текста)
    keyText = []
    for i in range(textLen // gammaLen):
        for symb in gamma:
            keyText.append(symb)
    for i in range(textLen % gammaLen):
        keyText.append(gamma[i])

    #Шифрование
    code = []
    for i in range(textLen):
        code.append(alphabeth[(alphabeth.index(text[i]) + alphabeth.index(keyText[i])) % 26])

    return code
a = input("Введите латинский текст ")
b = input("Введите ключ ")
print(encrypt(a,b))