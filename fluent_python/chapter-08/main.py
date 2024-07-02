from typing import Any, Optional, Protocol, TypeVar
from collections.abc import Iterable
from decimal import Decimal


class Bird:
    pass

class Duck(Bird):
    def quack(self):
        print("Quak!!!!!")
        
# Error 
# def alert(birdie):
#     return birdie.quack()

def alert_duck(birdie: Duck) -> None:
    return birdie.quack()

alex = Duck()
# alert(alert)
alert_duck(alex)


def show_count(count: int, singular: str, plural: Optional[str] = None) -> str:
    pass

# plural: str | None up to V3.10
# plural: Optional[str] below V3.10


def display(lat_long: tuple[float, float]) -> str:
    lat, lon = lat_long
    ns = "N" if lat >= 0 else "S"
    ew = "E" if lon >= 0 else "W"
    return f"{abs(lat):0.1f} {ns}, {abs(lon):0.1f} {ew}"

# ----------------------------------------------------
from replacer import zip_replace
l33t = [('a', '4'), ('e', '3'), ('i', '1'), ('o', '0'), ('d', '8')]
text = 'mad skilled noob powned leet code call of duty schema'

print(zip_replace(text, l33t))

# Only numbers
NUMBER_T = TypeVar("NUMBER_T", float, int , Decimal)

def mode(sequence: Iterable[NUMBER_T]):
    pass

class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool:
        pass

LT = TypeVar("LT", bound=SupportsLessThan)

def top(series: Iterable[LT], lenght:int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:lenght]

l = 'mango pear apple kiwi banana'.split()
ln = [3 ,2 , 0 , 2 , 2 , 2 , 4 , 2 ]
print(top(l, 3))
print(top(ln, 2))