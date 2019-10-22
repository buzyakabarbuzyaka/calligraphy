# coding: utf8

ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
N = len(ALPHABET)
TABLE = [ALPHABET[i::] + ALPHABET[0:i:] for i in range(N)]


def format_string(to_format):
    return "".join(letter for letter in to_format.upper() if ALPHABET.find(letter) >= 0)


def tirimey_encrypt(message_to_encode):
    message_to_encode_formated = format_string(message_to_encode)

    encrypted_message = []
    for index_in_message, letter in enumerate(message_to_encode_formated):
        line = index_in_message % len(ALPHABET)
        column = ALPHABET.find(letter)
        encrypted_message += TABLE[line][column]

    return "".join(encrypted_message)


def tirimey_decrypt(message_to_decode):
    message_to_decode_formated = format_string(message_to_decode)

    decrypted_message = []
    for index_in_message, letter in enumerate(message_to_decode_formated):
        line = index_in_message % len(ALPHABET)
        column = TABLE[line].find(letter)
        decrypted_message += ALPHABET[column]

    return "".join(decrypted_message)


if __name__ == '__main__':
    print(*TABLE, sep="\n")
    msg = "АБВ"
    tmp = tirimey_encrypt(msg)
    print(tmp)
    print(tirimey_decrypt(tmp))
