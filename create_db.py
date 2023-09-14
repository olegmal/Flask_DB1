import sqlite3

# def connect(query):
with sqlite3.connect("store_db.sqlite") as connection:
    cursor = connection.cursor()
    cursor.execute()
    result = cursor.fetchall()



def creation_table():
    query_1 = """
                CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name VARCHAR(30), 
                last_name VARCHAR (40)
                )
            """

    cursor.execute(query_1)

    query_2 = """
                    CREATE TABLE tracks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name VARCHAR(80), 
                    duration INTEGER)
                """

    cursor.execute(query_2)


    query_3 = """
            INSERT INTO tracks (id, name, duration)
            VALUES(1, 'LA GRANGE', 6), (2, 'WONDERFUL TONIGHT', 3), (3, 'FAST LIFE RIDER', 4),(4, 'THIS LAND', 4)
        """

    cursor.execute(query_3)

    query_4 = """
                INSERT INTO customers (id, first_name, last_name)
                VALUES(1, 'Jane', 'Dow'), (2, 'Viktor', 'Mahony'), (3, 'Wayne', 'Gretzkey'),(4, 'Viktor', 'Malowny')
            """

    cursor.execute(query_4)