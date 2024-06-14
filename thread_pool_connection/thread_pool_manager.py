import psycopg2
from psycopg2 import pool
from config import config


class PostgresDB:
    CONN_POOL = None

    def __init__(self) -> None:
        if PostgresDB.CONN_POOL is None:
            raise Exception("Connection pool is not initialized")
        print("Constructor initialized")
        self.ps_connection = PostgresDB.CONN_POOL.getconn()
        if self.ps_connection is None:
            raise Exception("Failed to obtain connection from the pool")

    def __del__(self):
        print("Destructor called")
        if self.ps_connection:
            PostgresDB.CONN_POOL.putconn(self.ps_connection)

    def connection_check(self) -> bool:
        try:
            if self.ps_connection:
                cursor = self.ps_connection.cursor()
                cursor.execute("SELECT 1")
                cursor.close()
                print("Successfully received connection from connection pool")
                return True
        except Exception as e:
            print("Connection health is not safe", e)
        return False

    def close_connection(self, cursor):
        try:
            cursor.close()
            print("Successfully closed cursor")
        except Exception as e:
            print("Something went wrong", e)

    @classmethod
    def create_pool(cls):
        params = config()
        try:
            cls.CONN_POOL = psycopg2.pool.ThreadedConnectionPool(5, 20, **params)
            print("Connection pool created successfully using ThreadedConnectionPool")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)

    @classmethod
    def release_pool(cls):
        if cls.CONN_POOL:
            cls.CONN_POOL.closeall()
            print("Closed connection pool")

    def read_data(self, query):
        try:
            if self.connection_check():
                cursor = self.ps_connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                data = [dict(zip([key[0] for key in cursor.description], row)) for row in result]
                self.close_connection(cursor)
                return data
        except (Exception, psycopg2.DatabaseError) as error:
            print("Something went wrong", error)
            return "Error reading data"

        return "No connection"

    def update_data(self, query):
        try:
            if self.connection_check():
                cursor = self.ps_connection.cursor()
                cursor.execute(query)
                self.close_connection(cursor)
                self.ps_connection.commit()
                return True            
        except (Exception, psycopg2.DatabaseError) as error:
            print("Something went wrong", error)
            return False

        return "No connection"

    def write_data(self, query):
        try:
            if self.connection_check():
                cursor = self.ps_connection.cursor()
                cursor.execute(query)
                self.close_connection(cursor)
                self.ps_connection.commit()
                return True            
        except (Exception, psycopg2.DatabaseError) as error:
            print("Something went wrong", error)
            return False

        return "No connection"
