TRANSLIT_DICTONARY = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e",
    "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m",
    "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
    "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch",
    "ы": "y", "ъ": "", "э": "e", "ю": "yu", "я": "ya", "ь": ""}


def translit(family):
    """Gets str translit it and returns str"""
    for key in TRANSLIT_DICTONARY:
        family = family.lower().replace(key, TRANSLIT_DICTONARY[key])
    return " ".join([i.capitalize() for i in family.split()])


print(translit('Павленко Евгений Валентинович'))
