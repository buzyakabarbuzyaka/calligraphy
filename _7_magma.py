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


# TODO: доделать циклический сдвиг
def cyclic_bit_move(hex_str: str, num_of_bits: int):
    """n>0: >>
        n<0: <<"""
    num_of_bytes = ceil(num_of_bits / 8)


def magma_encode(message_to_encode):
    converted_msg = bytearray(message_to_encode, encoding="utf8").hex()
    encrypted_msg = []
    for i, b in enumerate(converted_msg):
        encrypted_msg += CRYPT_TABLE[i % N][int(b, 16)]
    return "".join(encrypted_msg)


def magma_decode(message_to_decode):
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
