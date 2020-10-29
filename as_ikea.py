"""Make your last name sound as an Ikea product.

As seen in https://www.facebook.com/max.abelev/posts/3347430315294332
"""

import random


def as_ikea(name: str) -> str:
    """
    Convert letters to ikea letters
    :param: string
    :return: ikea string
    """
    mapper = dict(a=["à", "á", "â", "ä", "æ", "ã", "ā"],
                  o=["ô", "ö", "ò", "ó", "œ", "ø", "ō"],
                  u=["û", "ü", "ù", "ú", "ū"],
                  e=["è", "é", "ê", "ë", "ē", "ė"])

    for index, letter in enumerate(name.lower(), start=0):
        if mapper.get(letter):
            name = replacer(name, random.choice(mapper[letter]), index)

    return name[::-1].title()


def replacer(s: str, newstring: str, index: int, nofail: bool = False) -> str:
    """
    String replacer at certain index
    :param: string, new string, index
    :return: new string
    """
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]


#assert as_ikea("Ivanov") == 'Vönävi'

if __name__ == "__main__":
    print(as_ikea('Abelev'))
    
# Change next:
#  - can you write a pseudocode for this procedure?
#  - add more tests that fail
#  - use proper capitalisation with .lower() and .capitalize()   
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
