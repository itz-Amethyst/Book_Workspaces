from weakref import WeakKeyDictionary
# class Grade:
#     def __init__(self) -> None:
#         self.grade = 0
        
#     @property
#     def grade(self):
#         return self.grade
#     @grade.setter
#     def grade(self, value:str):
#         if not (0<= value <= 100):
#             raise ValueError("must be between 0 and 100")
        
#         self.grade = value


class Grade:
    def __init__(self) -> None:
        self.values = WeakKeyDictionary() 
        
        
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self.values.get(instance, 0)
    def __set__(self, instance, value):
        if not (0<= value <= 100):
            raise ValueError("must be between 0 and 100")
        
        self.values[instance] = value
    
    
class Exam:
    math = Grade()
    history = Grade()
    computer = Grade()

first_exam = Exam()
first_exam.math = 50
second_exam = Exam()
second_exam.computer = 90

print(f'first exam is {first_exam.math}')
print(f'second exam is {second_exam.computer}')