# coding: utf8

str = """X А Б В Г Д Е Ж З И Й К Л М Н О П
Y Г Д Е Ж З И Й К Л М Н О П Р С Т
i 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
X Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я
Y У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я А Б В
i 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32"""

lines = str.split("\n")
lines = [line.split() for line in lines]
lines = [line[1:] for line in lines]

_question = [lines[0::2]]
_question = "".join(_question)

_alph = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
_ans = 'ГДЕЖЗИЙКЛМНОПРСТФХЦЧШЩЪЫЬЭЮЯАБВ'

"""Г Д Е Ж З И Й К Л М Н О П Р С Т Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я А Б В"""
