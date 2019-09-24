# coding: utf8

ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
N = len(ALPHABET)


def atbash(dat):
    ans = ""
    for c in dat:
        i = ALPHABET.find(c.upper())
        if i < 0:
            ans += c
        else:
            if c == c.upper():
                ans += ALPHABET[N - i - 1]
            else:
                ans += (ALPHABET[N - i - 1]).lower()

    return ans


if __name__ == "__main__":
    # ===
    assert atbash("АБВ") == "ЯЮЭ", print('ans:', atbash("АБВ"))
    # ===
    _question = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    _ans = 'ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЕДГВБА'
    assert atbash(_question) == _ans, print("ans:", atbash(_question))
