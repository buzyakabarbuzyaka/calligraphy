# coding: utf8
from calligraphy._5_Belazo import belazo_encrypt, belazo_decrypt


def vijner_encrypt(message_to_encrypt, key_letter: str):
    return belazo_encrypt(message_to_encrypt, key_letter + message_to_encrypt)


def vijner_decrypt(message_to_decrypt, key_letter: str):
    current_key_letter = key_letter
    decrypted_message = []
    for letter in message_to_decrypt:
        current_key_letter = belazo_decrypt(letter, current_key_letter)
        decrypted_message += current_key_letter

    return "".join(decrypted_message)


def vijner_double_encrypt(message_to_encrypt, key_letter: str):
    pass

def vijner_double_decrypt(message_to_decrypt, key_letter: str):
    pass


if __name__ == '__main__':
    print(vijner_encrypt("ЖОПА", "Л"))
    print(vijner_decrypt("СФЭП", "Л"))
