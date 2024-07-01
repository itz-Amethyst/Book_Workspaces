from typing import NamedTuple, Optional
from dataclasses import dataclass, field
from enum import Enum, auto
from datetime import date
# class Coordinate(NamedTuple):
# this will make the instances immutable
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

    def __str__(self):
        ns = "N" if self.lat >= 0 else "S"
        we = "W" if self.lon>= 0 else "E"
        return f"{abs( self.lat ):.1f} {ns} , {abs(self.lon):.1f} {we}"
    
    
tehran = Coordinate(lat=56.532525, lon=23.0000)
tehran2 = Coordinate(lat=56.532525, lon=23.0000)

print(tehran == tehran2)

# ---------------------------

class ResourceType(Enum):
    BOOK  = auto() 
    EBOOK = auto()
    VIDEO = auto()
    
@dataclass
class Resource:
    identifire: str
    title: str = '<untitled>'
    creators: list[str] = field(default_factory=list)
    date: Optional[date] = None
    type: ResourceType = ResourceType.BOOK
    description: str = ''
    language: str = ''
    subjects: list[str] = field(default_factory=list)

r = Resource('0')
description = 'Improving the design of existing code'
book = Resource('978-0-13-475759-9', 'Refactoring, 2nd Edition',
                ['Martin Fowler', 'Kent Beck'], date(2018, 11, 19),
                ResourceType.BOOK, description,
                'EN', ['computer programming', 'OOP'])
print(book)
