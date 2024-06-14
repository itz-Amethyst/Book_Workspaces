import time
from thread_pool_manager import PostgresDB
start_time = time.perf_counter()

PostgresDB.create_pool()

pgdb = PostgresDB()

for i in range(10000):
    response = pgdb.write_data("INSERT INTO public.names(pk, language_name, rating) VALUES ({}, 'Python',200)")

# around 3 ~ 4 sec
print("Time taken to insert 1000 queries : (in second) ", time.perf_counter() - start_time)
print('Insertion status ->', response)