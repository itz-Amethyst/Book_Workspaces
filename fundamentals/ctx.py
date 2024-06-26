from sqlite3 import connect
from contextlib import contextmanager

# creating manual ctx manager
# class contextmanager:
#     def __init__(self, gen) -> None:
#         self.gen = gen
#     def __call__(self, *args, **kwargs):
#         self.args, self.kwargs = args, kwargs
#         return self
#     def __enter__(self):
#         self.gen_inst = self.gen(*self.args, **self.kwargs)
#         next(self.gen_inst)
#     def __exit__(self, *args):
#         next(self.gen_inst, None)

@contextmanager
def temptable(curs):
    curs.execute("CREATE TABLE IF NOT EXISTS temp (x int, y int)")
    yield
    curs.execute('drop table temp')

with connect(":memory:") as conn:
    curs = conn.cursor()
    with temptable(curs):
        curs.execute('INSERT INTO temp VALUES (1, 2)') 
        curs.execute('INSERT INTO temp VALUES (4, 6)') 
        curs.execute('INSERT INTO temp VALUES (6, 2)') 
        for row in curs.execute('SELECT x, y FROM temp'):
            print(row)
        
        for row in curs.execute('SELECT sum(x + y) from temp'):
            print(row)