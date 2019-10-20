# coding: utf8

ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
N = len(ALPHABET)
TABLE = [ALPHABET[i::] + ALPHABET[0:i:] for i in range(N)]
NAVIGATOR = dict(zip(list(ALPHABET), TABLE))


def format_string(to_format):
    return "".join(letter for letter in to_format.upper() if ALPHABET.find(letter) >= 0)


def form_table(password):
    table = []
    for letter in password:
        i = ALPHABET.find(letter)
        table += [ALPHABET[i::] + ALPHABET[:i:]]
    return table


def generate_password_underline(gen_line_len, password_format):
    repetitions_count = gen_line_len // len(password_format)
    left_symbols_count = gen_line_len % len(password_format)
    return "".join([password_format * repetitions_count]) + password_format[:left_symbols_count:]


def belazo_encrypt(message_to_encrypt, password: str):
    password_formated = format_string(password)
    message_to_encrypt_formated = format_string(message_to_encrypt)

    generating_line = generate_password_underline(len(message_to_encrypt_formated), password_formated)

    encrypted_message = []
    for index, (msg_letter, gen_letter) in enumerate(zip(message_to_encrypt_formated, generating_line)):
        encrypted_message += NAVIGATOR[gen_letter][ALPHABET.find(msg_letter)]

    return "".join(encrypted_message)


def belazo_decrypt(message_to_decrypt, password: str):
    password_formated = format_string(password)
    message_to_decrypt_formated = format_string(message_to_decrypt)

    generating_line = generate_password_underline(len(message_to_decrypt_formated), password_formated)

    decrypted_message = []
    for index, (msg_letter, gen_letter) in enumerate(zip(message_to_decrypt_formated, generating_line)):
        decrypted_message += ALPHABET[NAVIGATOR[gen_letter].find(msg_letter)]

    return "".join(decrypted_message)


if __name__ == '__main__':
    print(belazo_encrypt("криптография", "зонд"))
    print(belazo_decrypt("СЮХУЩЬРФЗБХВ", "зонд"))
