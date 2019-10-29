# coding: utf8


def remove_symbols(to_format: str):
    return "".join([c for c in to_format if (c.lower() != c.upper())])
