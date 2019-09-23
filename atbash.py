ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
N = len(ALPHABET)


def atbash(dat):
    ans = ""
    for c in dat:
        if c == " ":
            ans += " "
            continue
        i = ALPHABET.find(c.upper())
        if i < 0:
            continue
        ans += ALPHABET[N - i - 1]
    return ans


if __name__ == "__main__":
    # ===
    assert atbash("АБВ") == "ЯЮЭ", print("ans:", atbash("АБВ"))
    # ===
    _question = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    _ans = 'ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЕДГВБА'
    assert atbash(_question) == _ans, print("ans:", atbash(_question))
