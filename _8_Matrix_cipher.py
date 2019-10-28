# coding: utf8
import numpy as np
from math import ceil


class MatrixError(Exception):
    pass


def remove_symbols(to_format: str):
    return "".join([c for c in to_format if (c.lower() != c.upper()) or c == ' '])


def supplement_vector(index_array, matrix_size: int):
    num_of_zeros_to_add = ceil(index_array.size / matrix_size) * matrix_size - index_array.size
    return np.zeros((num_of_zeros_to_add,), dtype=int)


def matrix_encode_rus(message_to_encode: str, matrix):
    format_matrix = np.array(matrix, dtype=int)

    try:
        np.linalg.inv(format_matrix)
    except Exception as exc:
        raise MatrixError("Матрица не имеет обратной")

    # format_msg = remove_symbols(message_to_encode).upper()
    format_msg=message_to_encode  # Без форматирования тоже работает
    index_array = np.array([ord(c) - ord('А') + 1 for c in format_msg], dtype=int)
    index_array = np.concatenate((index_array, supplement_vector(index_array, format_matrix.shape[0])))
    n = format_matrix.shape[0]

    ans = np.array([format_matrix.dot(index_array[i:i + n:]) for i in range(0, index_array.size, n)])
    ans = ans.reshape((ans.size,))
    return ans.tolist()


def matrix_decode_rus(message_to_decode, matrix):
    format_matrix = np.array(matrix)
    try:
        inv_format_matrix = np.linalg.inv(format_matrix)
    except Exception as exc:
        raise MatrixError("Матрица не имеет обратной")
    format_msg = np.array(message_to_decode)
    n = inv_format_matrix.shape[0]
    ans = np.array(
        [list(map(lambda x: int(round(x)), inv_format_matrix.dot(format_msg[i:i + n:]))) for i in
         range(0, format_msg.size, n)], dtype=int)
    ans = ans.reshape((ans.size,)).tolist()
    ans = [i for i in ans if i != 0]
    return "".join([chr(ord("А") + i - 1) for i in ans])


if __name__ == '__main__':
    mtrx = [[1, 4, 8],
            [3, 7, 2],
            [6, 9, 5]]
    ans = matrix_encode_rus("ЗАБАВА ЗАБАВАбlkm;l,09-", mtrx)
    print(ans)
    print(matrix_decode_rus(ans, mtrx))
