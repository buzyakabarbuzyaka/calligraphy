# coding: utf8

ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
N = len(ALPHABET)


def cezar_encode(dat, shift=0):
    ans = ""
    for c in dat:
        i = ALPHABET.find(c.upper())
        ans += ALPHABET[(i + shift) % N]
    return ans


def cezar_decode(dat, shift=0):
    return cezar_encode(dat, -shift)


if __name__ == "__main__":
    # ===
    _question = 'АБВ'
    _ans = 'ГДЕ'
    assert cezar_encode(_question) == _ans, print("ans:", cezar(_question))

    # ===
    _question = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    _ans = 'ГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ'
    assert cezar_encode(_question) == _ans, print("ans:", cezar(_question), _ans)
