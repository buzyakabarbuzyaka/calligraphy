# coding: utf8
from calligraphy.opt import remove_symbols
from math import ceil


def code_list(word: str):
    key_list = list(enumerate(list(word)))
    sorted_key_list = sorted(key_list, key=lambda x: x[1])
    navigator = dict([(hi, lo + 1) for lo, hi in enumerate(sorted_key_list)])
    return [navigator[key] for key in key_list]


def feat_into_table(msg: list, columns):
    msg += [" "] * (ceil(len(msg) / columns) * columns - len(msg))
    ans = [msg[i:i + columns:] for i in range(0, len(msg), columns)]
    for i in range(1, len(ans), 2):
        ans[i] = ans[i][::-1]
    return ans


def transpose(table: list):
    table_cols, table_raws = len(table[0]), len(table)
    ans = [[0] * table_raws for _ in range(table_cols)]
    for i in range(table_raws):
        for j in range(table_cols):
            ans[j][i] = table[i][j]

    return ans


def reverse_feat_into_table(msg: list, columns):
    rows = len(msg) // columns
    tmp = transpose(feat_into_table(msg, rows))
    return [line[::-1] for line in tmp]


def vertical_permutation_encode(message_to_encode, columns=7):
    format_msg_to_encode = list(remove_symbols(message_to_encode).upper())
    table = feat_into_table(format_msg_to_encode, columns)
    ans = []
    for i in range(columns - 1, -1, -1):
        if i % 2 == 0:
            ans += [line[i] for line in table]
        else:
            ans += [line[i] for line in table][::-1]
    return "".join(ans)


def vertical_permutation_decode(message_to_decode, columns=7):
    tmp = reverse_feat_into_table(list(message_to_decode), columns)
    rows=len(message_to_decode)//columns
    ans = []
    for i in range(rows):
        if i % 2 == 0:
            ans += tmp[i]
        else:
            ans += tmp[i][::-1]
    return "".join(ans).strip()

# TODO: доделать с ключем
if __name__ == '__main__':
    print(vertical_permutation_encode("пример маршрутной перестановки хех"))
    print(vertical_permutation_decode("МАСТ  АЕРРЕШРН  ОЕРМИУПВХЕКЙТРПНОИХ", 7))
