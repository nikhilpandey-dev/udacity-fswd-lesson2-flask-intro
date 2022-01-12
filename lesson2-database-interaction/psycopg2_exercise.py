import psycopg2
from config import config

try:
    params = config()
    print(params)
    connection = psycopg2.connect(**params)
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS table2')
    cursor.execute("""
        CREATE TABLE table2(
                id SERIAL PRIMARY KEY,
                completed BOOLEAN NOT NULL DEFAULT False
            );
    """)
    cursor.execute('''INSERT INTO table2 (completed) VALUES (true);
    ''')

    cursor.execute('INSERT INTO table2 (completed) VALUES (%s);', (False,))

    cursor.execute('INSERT INTO table2 (completed) VALUES (%(completed)s);', {
        'completed': False
    })

    cursor.execute("SELECT * FROM table2;")
    result = cursor.fetchall()

    for r in result:
        print(r)

    print(f"The rows in table 2 after fetch all are:\n{result}")
    connection.commit()

    cursor.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if connection is not None:
        connection.close()
        print('Database connection terminated')

