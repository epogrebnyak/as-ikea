"""Make your last name sound as an Ikea product.

As seen in https://www.facebook.com/max.abelev/posts/3347430315294332
"""

def as_ikea(name: str) -> str:
    mapper = dict(a="ä", o="ö", u="ü")
    for letter in mapper.keys():
       name = name.replace(letter, mapper[letter])
    return name[::-1]

assert as_ikea("Ivanov") == 'Vönävi' #fails

# Change next:
#  - can you write a pseudocode for this procedure?
#  - add more tests that fail
#  - use proper capitalisation with .lower() and .capitalize()   
#  - should there be just one letter change?
#  - inquire about "Umalut". Is our substitute algorith ok?
#    https://ru.wikipedia.org/wiki/%D0%A3%D0%BC%D0%BB%D0%B0%D1%83%D1%82
#  - what about "å"?
#  - does code need more refactoring?

# Possible more serious questions:
#  - how we can get real array of Ikea products?
#  - can we make a properly sounding generative model for the products?
#  - does product naming affect market success? See eg https://www.esic.edu/documentos/revistas/esicmk/1574698527_I.pdf
#  - is there A/B test evidence for this that?
