# coding: utf8

import random

alphavit = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4,
            'е': 5, 'ж': 6, 'з': 7, 'и': 8, 'й': 9,
            'к': 10, 'л': 11, 'м': 12, 'н': 13, 'о': 14,
            'п': 15, 'р': 16, 'с': 17, 'т': 18, 'у': 19,
            'ф': 20, 'х': 21, 'ц': 22, 'ч': 23, 'ш': 24,
            'щ': 25, 'ъ': 26, 'ы': 27, 'ь': 28, 'э': 29,
            'ю': 30, 'я': 31, ' ': 32, ",": 33, ".": 34
            }


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

if __name__ == '__main__':
    msg = input("Введите текст:")
    message = list(msg)
    message_len = len(message)
    msg_code_bin_list = list()
    for i in range(len(message)):
        msg_code_bin_list.append(alphavit.get(message[i]))
    print();
    print("Текст:={}".format(msg_code_bin_list))
    key_list = list()
    for i in range(message_len):
        key_list.append(random.randint(0, 50))
    print();
    print("Ключ:={}".format(key_list))
    print();
    cipher_list = list()

    # шифрование по с = m xor k
    for i in range(message_len):
        m = int(msg_code_bin_list[i])
        k = int(key_list[i])
        cipher_list.append(int(bin(m ^ k), base=2))
    print("Шифр:={}".format(cipher_list))
    print();
    # расшифрование по m = c xor k
    decipher_list = list()
    for i in range(message_len):
        c = int(cipher_list[i])
        k = int(key_list[i])
        decipher_list.append(int(bin(c ^ k), base=2))

    deciphered_str = ""
    for i in range(len(decipher_list)):
        deciphered_str += get_key(alphavit, decipher_list[i])

    print("Расшифрованный код:={}".format(decipher_list))
    print();
    print("Расшифрованный текст:={}".format(deciphered_str))
