metro_areas = [
('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def print_loc_long(metro_areas):
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name , _ , _ , (lat, long) in metro_areas:
        if long <= 10:
            print("{name:15} | {lat:9.4f} | {long:9.4f}".format(name=name, lat=lat, long=long))
            
        
print_loc_long(metro_areas)

class Language:
    def __init__(self, name, level) -> None:
        self.name = name
        self.level= level

# also can be handled by functools singledispatch
def handle_command(data):
    match data:
        
        case {
            "type": "language",
            "name": str(name),
            "level": str(level)
        } if level == "High" or level == "Low":
            print("type: dict handling")
        
        case int():
            print("type: int, handling")
        
        case [
            str(name),
            *_ ,# anything from name until last doesnt matter (middle)
            (float(rating), float(reddit_count))
        ]:
            print("type: list handling")
           
        case Language(name = str(name), level = str(level)) as language:
            print("type: language", name, level , language)
           
        case _:
            raise ValueError("Incorrect value type")

handle_command({"type": "language", "name": "python", "level": "High"})
handle_command(["Konichiwa", 35,  32523 ,(35.689722, 139.691667)])
handle_command(325325)
handle_command(Language(name="Go", level="Low"))
#! will throw an ValueError
# handle_command(["username"])