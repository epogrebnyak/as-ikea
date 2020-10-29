# as-ikea
Convert your name to Ikea product name

```python
def as_ikea(name: str) -> str:
    mapper = dict(a="ä", o="ö", u="ü")
    for letter in mapper.keys():
       name = name.replace(letter, mapper[letter])
    return name[::-1]
```
Code source and discussion [here](as_ikea.py)

![](https://user-images.githubusercontent.com/9265326/97590229-75e97d80-1a0f-11eb-9878-e4139565b459.png)
