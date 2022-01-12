import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT, ISOLATION_LEVEL_DEFAULT
from config import config
from typing import List, Dict, Tuple
# print(psycopg2.__doc__)
# fsnd_psycopg2_example

def connect():
    connection: psycopg2.connection = None
    try:
        params: Dict[str, str] = config()
        print('Conneecting to PostgreSQL Database ...')
        connection = psycopg2.connect(**params)
        #  Create a cursor
        cursor: psycopg2.cursor = connection.cursor()
        print('PostgreSQL dtabase version: ')
        cursor.execute('SELECT version();')
        db_version = cursor.fetchone()
        print(db_version)
        cursor.execute("DROP TABLE IF EXISTS todos")
        cursor.execute("""
            CREATE TABLE todos (
                id SERIAL PRIMARY KEY,
                description VARCHAR NOT NULL
            );
        """)

        """ Since we are letting the SQL insert id, so our table has only the single element and for this we need to create a single element tuple, which is done by Tuple(element, ), i.e., To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple. """
        cursor.execute("INSERT INTO todos (description) VALUES (%s);", ("To complete Full Stack Nanodegree and complete my app", ))
        cursor.execute("INSERT INTO todos (description) VALUES (%s);", ("To launch my app", ))
        data: Dict[str, str] = {
            'description': 'To start working on the RiskDoctor App API structure & complete it'
        }
        sql_statement = "INSERT INTO todos (description) VALUES (%(description)s);"
        cursor.execute(sql_statement, data)
        cursor.execute("SELECT * FROM todos;")
        result = cursor.fetchmany(2)
        print(result)
        result2 = cursor.fetchone()
        print('fetchone', result2)
        result3 = cursor.fetchone()
        print('fetchone', result3)
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database conncection terminated.')

if __name__ == "__main__":
    connect()



# try:
#     connection = psycopg2.connect("dbname='fsnd_psycopg2_example' user='postgres' host='localhost' password='wework_sector40'")
# except:
#     print("Could not connect to database")

# cursor = connection.cursor()
# cursor.execute("""
#     CREATE TABLE table1 (
# 	id SERIAL PRIMARY KEY,
# 	completed Boolean NOT NULL DEFAULT FALSE
# );
# """)
# print(f"Created Table table1")

# cursor.execute("""
#     INSERT INTO table1 (completed) VALUES (True);
# """)
# connection.commit()
# cursor.close()
# connection.close()