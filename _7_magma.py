# coding: utf8
from math import ceil

CRYPT_TABLE = ["c462a5b9e8d703f1",
               "68239a5c1e47bd0f",
               "b3582fade174c960",
               "c821d4f670a53e9b",
               "7f5a816d093eb42c",
               "5df692cab78143e0",
               "8e25691cf4b0da37",
               "17ed05834fa69cb2"]
N = len(CRYPT_TABLE)


def cyclic_left(hex_str: str, nbits: int):
    if hex_str == "":
        return ""

    num_of_bits_in_str = len(hex_str) * 4
    nbits = nbits % num_of_bits_in_str
    num = int(hex_str, 16)
    tail = num >> num_of_bits_in_str - nbits
    front = tail << num_of_bits_in_str
    return "{:x}".format(((num << nbits) | tail) ^ front)


def cyclic_right(hex_str: str, nbits: int):
    if hex_str == "":
        return ""

    num_of_bits_in_str = len(hex_str) * 4
    nbits = nbits % num_of_bits_in_str
    addition = 2 ** num_of_bits_in_str  # добавление незначащих битов
    num = int(hex_str, 16)
    num = num | addition

    tail = (num >> nbits) ^ (addition >> nbits)
    front = tail << num_of_bits_in_str
    nbits_to_left = num_of_bits_in_str - nbits
    return "{:x}".format((((num << nbits_to_left) | tail) ^ front) ^ (addition << nbits_to_left))


def magma_encode(message_to_encode):
    converted_msg = bytearray(message_to_encode, encoding="utf8").hex()
    encrypted_msg = []
    for i, b in enumerate(converted_msg):
        encrypted_msg += CRYPT_TABLE[i % N][int(b, 16)]
    tmp = "".join(encrypted_msg)
    return cyclic_left(tmp, 11)


def magma_decode(message_to_decode):
    message_to_decode = cyclic_right(message_to_decode, 11)
    print(message_to_decode)
    decrypted_msg = []
    for i, b in enumerate(message_to_decode):
        decrypted_msg.append(CRYPT_TABLE[i % N].find(b))
    hex_decrypted_msg = "".join([h[-1] for h in map(hex, decrypted_msg)])  # TODO: Сделать без конкатенации символов
    return bytearray.fromhex(hex_decrypted_msg).decode("utf8")


if __name__ == '__main__':
    msg = "ПИСЯ"

    tmp = magma_encode(msg)
    print(tmp)
    print(magma_decode(tmp))
