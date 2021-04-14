import re

punctuation = [".", ",", "!", "?", ":", ";", "&", '"', "@", "#", "(", ")" ]


def pad_string(unpadded_str):
    padded_str = f" {unpadded_str} "
    for c in punctuation:
        padded_str = padded_str.replace(c, f" {c} ")
    return padded_str


def unpad_string(str):
    str = str.replace("  ", " ")
    str = str.strip()
    for c in punctuation:
        str = str.replace(" " + c, c)
    return str


def remove_end_punctuation(str):
    str = str.strip()
    if str[len(str)-1] in punctuation:
        return str[:-1]
    return str


def get_text_after_keyword(text, keyword):
    expr = f".*?{keyword}"
    res = re.sub(expr, "", text, flags=re.IGNORECASE)
    return res