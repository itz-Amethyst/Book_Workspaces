from functools import singledispatch

@singledispatch
def process(s):
    raise NotImplementedError("Invalid Type")

@process.register(int)
def _(data):
    return data * 2 

@process.register(str)
def _(data):
    return data.upper()

@process.register(list)
def _(data):
    return  [process(item) for item in data]

@process.register(bool)
def _(data):
    return  not data


print(process(5)) # 10
print(process("Hello world")) # HELLO WORLD
print(process([5, "Milad", 50])) # [10, 'MILAD', 100]
print(process(True)) # False

### Class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
@singledispatch
def calculate_area(obj):
    raise NotImplemented("Unsupported object")

@calculate_area.register(Circle)
def _(obj):
    return math.pi * obj.radius ** 2

@calculate_area.register(Rectangle)
def _(obj):
    return obj.width * obj.height 

circle = Circle(10)
rectangle = Rectangle(width= 50, height=20)

print(calculate_area(circle))
print(calculate_area(rectangle))