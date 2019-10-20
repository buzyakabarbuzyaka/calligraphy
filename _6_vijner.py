# coding: utf8

ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
N = len(ALPHABET)
TABLE = [ALPHABET[i::] + ALPHABET[0:i:] for i in range(N)]
NAVIGATOR = dict(zip(list(ALPHABET), TABLE))


def format_string(to_format):
    return "".join(letter for letter in to_format.upper() if ALPHABET.find(letter) >= 0)


def vijner_encrypt(message_to_encrypt, password: str):
    pass


def vijner_decrypt(message_to_decrypt, password: str):
    pass


def vijner_double_encrypt(message_to_encrypt, password: str):
    pass


def vijner_double_decrypt(message_to_decrypt, password: str):
    pass


if __name__ == '__main__':
    pass
