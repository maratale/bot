TRANSLIT_DICT = {
    "А": "A", "а": "a",
    "Б": "B", "б": "b",
    "В": "V", "в": "v",
    "Г": "G", "г": "g",
    "Д": "D", "д": "d",
    "Е": "E", "е": "e",
    "Ё": "E", "ё": "e",
    "Ж": "Zh", "ж": "zh",
    "З": "Z", "з": "z",
    "И": "I", "и": "i",
    "Й": "I", "й": "i",
    "К": "K", "к": "k",
    "Л": "L", "л": "l",
    "М": "M", "м": "m",
    "Н": "N", "н": "n",
    "О": "O", "о": "o",
    "П": "P", "п": "p",
    "Р": "R", "р": "r",
    "С": "S", "с": "s",
    "Т": "T", "т": "t",
    "У": "U", "у": "u",
    "Ф": "F", "ф": "f",
    "Х": "Kh", "х": "kh",
    "Ц": "Ts", "ц": "ts",
    "Ч": "Ch", "ч": "ch",
    "Ш": "Sh", "ш": "sh",
    "Щ": "Shch", "щ": "shch",
    "Ы": "Y", "ы": "y",
    "Э": "E", "э": "e",
    "Ю": "Yu", "ю": "yu",
    "Я": "Ya", "я": "ya",
}

SPECIAL_CASES = {
    "Е": "Ye", "е": "ye",
    "Ё": "Ye", "ё": "ye",
    "Ю": "Yu", "ю": "yu",
    "Я": "Ya", "я": "ya",
}

def transliterate(text: str) -> str:
    result = []
    for word in text.split():
        latin_word = ""
        i = 0
        while i < len(word):
            ch = word[i]
            if ch in {"ь", "Ь"}:
                if i + 1 < len(word):
                    next_ch = word[i + 1]
                    if next_ch.lower() in TRANSLIT_DICT or next_ch.lower() in SPECIAL_CASES:
                        latin_word += "y"
                i += 1
                continue
            elif ch in {"ъ", "Ъ"}:
                i += 1
                continue
            if i == 0 and ch in SPECIAL_CASES:
                latin_word += SPECIAL_CASES[ch]
            else:
                latin_word += TRANSLIT_DICT.get(ch, ch)
            i += 1
        result.append(latin_word)
    return " ".join(result)
