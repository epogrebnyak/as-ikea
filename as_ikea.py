"""Make your last name sound as an Ikea product name.

As seen in https://www.facebook.com/max.abelev/posts/3347430315294332
"""

import random
from typing import List
from transliterate import translit, get_available_language_codes, detect_language

# EP: note this is a very rich mapper, will convert every letter to
# something Swedish, this may not be the result you want as
# some names look cool with just one accented letter, not many letters
# like this.
#
# To enquire about "Umlaut" see https://ru.wikipedia.org/wiki/%D0%A3%D0%BC%D0%BB%D0%B0%D1%83%D1%82

mapper = dict(
    a=["à", "á", "â", "ä", "æ", "ã", "ā"],
    o=["ô", "ö", "ò", "ó", "œ", "ø", "ō"],
    u=["û", "ü", "ù", "ú", "ū"],
    e=["è", "é", "ê", "ë", "ē", "ė"],
)


def substitute(letter: str, mapper: dict = mapper) -> str:
    """
    Change 'a', 'o', 'u', 'e' to alternated variants randomly.
    """
    return random.choice(mapper[letter])


def reverse(s):
    return s[::-1]


def positions(name, mapper=mapper) -> List[int]:
    pos = []
    targets = mapper.keys()
    for i, letter in enumerate(name.lower()):
        if letter in targets:
            pos.append(i)
    return pos


def as_ikea(name: str) -> str:
    """
    Convert *name* to Ikea-like name.
    """
    # Replace just once
    name = name.lower()
    index = random.choice(positions(name))
    name = replace_at(name, index)
    return reverse(name).title()


def replace_at(name, index):
    new_letter = substitute(name[index])
    return replace_once(name, new_letter, index)


def replace_once(xs: str, x: str, i: int) -> str:
    """
    Insert *x* at position *i* in *xs*.
    """
    assert len(x) == 1
    return xs[:i] + x + xs[i + 1:]


def is_latin(s: str) -> bool:
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def to_latin(s: str) -> str:
    return translit(u'{}'.format(s), detect_lang(s), reversed=True)


def is_translit(s: str) -> bool:
    return detect_lang(s) in get_available_language_codes()


def detect_lang(s: str) -> str:
    return detect_language(u'{}'.format(s))


if __name__ == "__main__":
    lastname = "Абелев"
    if not is_latin(lastname):
        lastname = to_latin(lastname)

    print(as_ikea(lastname))

# Possible more serious applications:
#  - how we can get real array of Ikea products?
#  - does product naming affect market success? See eg https://www.esic.edu/documentos/revistas/esicmk/1574698527_I.pdf
#  - is there A/B test evidence for this that?

# Can the name be taken for Swedesh?
#  - can we make a properly sounding generative model for the products?
#  - can we calculate the likelyhood it is Swedish?
#  - what should be the probabilities of changing the letter (maybe due to position)?

# Ideas on web implementation:
#  - FastAPI for API
#  - something like Heroku for quick launch as a web service?

# For initial task (done):
#  - can you write a pseudocode for this procedure?
#  - add more tests that fail
#  - should there be just one letter change?
#  - does code need more refactoring?
