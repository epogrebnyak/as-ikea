"""Make your last name sound as an Ikea product name.

As seen in https://www.facebook.com/max.abelev/posts/3347430315294332
"""

import random


def substitute(letter: str) -> str:
    """
    Change 'a', 'o', 'u', 'e' to alternated variants.
    """
    mapper = dict(
        a=["à", "á", "â", "ä", "æ", "ã", "ā"],
        o=["ô", "ö", "ò", "ó", "œ", "ø", "ō"],
        u=["û", "ü", "ù", "ú", "ū"],
        e=["è", "é", "ê", "ë", "ē", "ė"],
    )
    return random.choice(mapper[letter])


def as_ikea(name: str) -> str:
    """
    Convert *name* to Ikea-like name.
    """
    for index, letter in enumerate(name.lower(), start=0):
        try:
            new_letter = substitute(letter)
            name = replace_once(name, new_letter, index)
        except KeyError:
            pass
    return name[::-1].title()


def replace_once(string: str, new_letter: str, index: int) -> str:
    """
    Insert *new_letter* at position *i* in *string*.
    """
    return string[:index] + new_letter + string[index + 1 :]


# assert as_ikea("Ivanov") == 'Vönävi'

if __name__ == "__main__":
    print(as_ikea("Abelev"))

# Change next:
#  - can you write a pseudocode for this procedure?
#  - add more tests that fail
#  - should there be just one letter change?
#  - inquire about "Umalut". Is our substitute algorith ok?
#    https://ru.wikipedia.org/wiki/%D0%A3%D0%BC%D0%BB%D0%B0%D1%83%D1%82
#  - what about "å"?
#  - does code need more refactoring?

# Possible more serious applications:
#  - how we can get real array of Ikea products?
#  - can we make a properly sounding generative model for the products?
#  - does product naming affect market success? See eg https://www.esic.edu/documentos/revistas/esicmk/1574698527_I.pdf
#  - is there A/B test evidence for this that?

# Ideas on implementation:
#  - FastAPI for API
#  - something like Heroku for quick launch as a web service?
