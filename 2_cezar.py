ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
N = len(ALPHABET)


def cezar(dat, shift=3):
    ans = ""
    for c in dat:
        i = ALPHABET.find(c.upper())
        ans += ALPHABET[(i + shift) % N]
    return ans


if __name__ == "__main__":
    # ===
    _question = 'АБВ'
    _ans = 'ГДЕ'
    assert cezar(_question) == _ans, print("ans:", cezar(_question))

    # ===
    _question = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    _ans = 'ГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ'
    assert cezar(_question) == _ans, print("ans:", cezar(_question), _ans)
