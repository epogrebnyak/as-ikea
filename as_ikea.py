"""Make your last name sound as an Ikea product name.

As seen in https://www.facebook.com/max.abelev/posts/3347430315294332
"""

import random

# EP: note this is a very rich mapper, will convert every letter to
# something Swedish, this may not be the result you want as
# some names look cool with just one accented letter, not many letters
# like this.
#
# To enquire about "Umalut" see https://ru.wikipedia.org/wiki/%D0%A3%D0%BC%D0%BB%D0%B0%D1%83%D1%82

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
    return reverse(name).title()


def replace_once(string: str, new_letter: str, index: int) -> str:
    """
    Insert *new_letter* at position *index* in *string*.
    """
    return string[:index] + new_letter + string[index + 1 :]


if __name__ == "__main__":
    print(as_ikea("Abelev"))

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
