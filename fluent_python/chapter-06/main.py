basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']

class SchoolBus:
    
    def __init__(self, passengers=[]) -> None:
        #! Without list it will violate "Principle of least astonishment" in fact will modify the basketball_team if we do any operation on it
        self.passangers = list(passengers)
            
    def pick(self, name):
        self.passangers.append(name)
            
    def drop(self, name):
        self.passangers.remove(name)
        
    def __repr__(self) -> str:
        return f"Members are : {self.passangers!r}"

final_bus = SchoolBus(basketball_team)
final_bus.pick("milad")
final_bus.drop("Sue")
print(final_bus)
print(basketball_team)