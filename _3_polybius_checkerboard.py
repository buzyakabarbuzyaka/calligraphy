# coding: utf8

CHECKERBOARD = ("АБВГДЕ",
                "ЖЗИЙКЛ",
                "МНОПРС",
                "ТУФХЦЧ",
                "ШЩЪЫЬЭ",
                "ЮЯ-")
N = len(CHECKERBOARD)
M = len(CHECKERBOARD[0])


def polybius_checkerboard_incode(input_str: str):
    processed_str = "".join([c.upper() if c != " " else "" for c in input_str])
    ans = []
    for c in processed_str:
        for i in range(N):
            j = CHECKERBOARD[i].find(c.upper())
            if j >= 0:
                ans.append(str(i + 1) + str(j + 1))
                break
        else:
            ans.append(c)
    return " ".join(ans)


def polybius_checkerboard_decode(input_str: str):
    # arr = [[int(c), int(s)] for c, s in input_str.split()]
    arr = input_str.split()
    ans = ""
    for pair in arr:
        ans += CHECKERBOARD[int(pair[0]) - 1][int(pair[1]) - 1]

    return ans.strip()


if __name__ == '__main__':
    assert polybius_checkerboard_incode("абв") == "11 12 13"
    assert polybius_checkerboard_incode("Выпущенное слово и камень не имеют возврата") == \
           "13 54 34 42 52 16 32 32 33 16 36 26 33 13 33 23 25 11 31 16 32 55 32 16 23 31 16 61 41 13 33 22 13 35 11 41 11"
    # =======
    assert polybius_checkerboard_decode("11 12 13") == "АБВ"
    assert polybius_checkerboard_decode(
        "13 54 34 42 52 16 32 32 33 16 36 26 33 13 33 23 25 11 31 16 32 55 32 16 23 31 16 61 41 13 33 22 13 35 11 41 11") \
           == "ВЫПУЩЕННОЕСЛОВОИКАМЕНЬНЕИМЕЮТВОЗВРАТА"
