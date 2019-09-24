# coding: utf8

import warnings
warnings.filterwarnings("ignore")

CHECKERBOARD = ['АБВГДЕ'
                'ЖЗИЙКЛ'
                'МНОПРС'
                'ТУФХЦЧ'
                'ШЩЪЫЬЭ'
                'ЮЯ-']

N = len(CHECKERBOARD)
M = len(CHECKERBOARD[0])


def polybius(dat):
    ans = []
    for c in dat:
        for i, line in enumerate(CHECKERBOARD):
            j = line.find(c.upper())
            if j != -1:
                ans += [str(i+1)+str(j+1)]
                break

    return " ".join(ans)


if __name__ == "__main__":
    func = polybius

    # ===
    _question = 'АБВ'
    _ans = '11 12 13'
    assert func(_question) == _ans, print("ans:", func(_question))

    # ===
    _question = 'Выпущенное слово и камень не имеют возврата'
    _ans = '13 54 34 42 52 16 32 32 33 16 36 26 33 13 33 23 25 11 31 16 32 55 32 16 23 31 16 61 41 13 33 22 13 35 11 41 11'
    assert func(_question) == _ans, print("ans:", func(_question))
