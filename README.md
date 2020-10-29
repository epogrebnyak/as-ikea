# as-ikea
Convert your name to Ikea product name

```python
def as_ikea(name: str) -> str:
    mapper = dict(a="ä", o="ö", u="ü")
    for letter in mapper.keys():
       name = name.replace(letter, mapper[letter])
    return name[::-1]
```

See code source and discussion [here](as_ikea.py).

Original idea, as heard from [this thread](https://www.facebook.com/max.abelev/posts/3347430315294332):

![](https://user-images.githubusercontent.com/9265326/97590229-75e97d80-1a0f-11eb-9878-e4139565b459.png)
