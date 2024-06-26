from time import sleep

def compute():
    for i in range(50):
        sleep(.5)
        yield i


for i in compute():
    rev = [i]
    print(i)



class Api:
    def first_func_create_super_user(self):
        """Should be run first method"""
        return "first"
    def second_func_retrive(self):
        """Should be run after first method"""
        return "second"
    
    def third_func_create_insert(self):
        """Should be run after second method"""
        return "third"

def api():
    """Gurantee order"""
    Api().first_func_create_super_user()
    yield
    Api().second_func_retrive()
    yield
    Api().third_func_create_insert()