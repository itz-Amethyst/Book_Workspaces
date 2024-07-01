from random import shuffle
from functools import partial
from operator import itemgetter, mul
from typing import Any

def factorial(number: int) -> int:
    """Return the factorial of the given number"""
    return 1 if number <= 1 else number * factorial(number - 1)

print(factorial.__doc__)


print(list(map(factorial, range(11))))

print([factorial(n) for n in range(6) if n % 2])

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda word: word[::-1]))



class Card:
    def __init__(self, items) -> None:
        self._items = list(items)
        shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty card deck")
        
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.pick()

french = Card(items = ['ACE', "HEART", "CLUB"])
print(french())

# -------------------------------------------------------

def html_tag(name, *content, class_=None, **attrs):
    """Generates html tags bassed on given inputs"""
    if class_ is not None:
        attrs["class"] = class_
        
    attr_pairs = (f' {attr}="{value}"' for attr , value in sorted(attrs.items()))
    attr_str = ''.join(attr_pairs)
    
    if content:
        elements = (f'<{name}{attr_str}>{c}</{name}>' for c in content)
        return '/n'.join(elements)
    else:
        return f"<{name}{attr_str} />"
    
print(html_tag('br'))
print(html_tag('p', 'hello word'))
print(html_tag('p', 'hello', 'word', 'earth'))
print(html_tag(name='img', src='./main.jpg', class_='12px'))
print(html_tag('p', 'hello', id=33))

# --------------------------------------------------------


metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

# Based on the second index which is JP or shorter version of the coutnry do the sorting operation
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)
print('----------------------------------')

# Q: Only need the 2 first information from metro_data
cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))


triple = partial(mul, 3)

print(list(map(triple, range(10))))