import sqlite3

def create_datebase(filename, create_query):
    with sqlite3.connect(filename) as conn:
        cu = conn.cursor()
        cu.execute(create_query)
        conn.commit()

def select_database(filename, select_query):
    with sqlite3.connect(filename) as conn:
        cu = conn.cursor()
        result = cu.execute(select_query)
        return result

def insert_database(filename, insert_query, tuple):
    with sqlite3.connect(filename) as conn:
        cu = conn.cursor()
        cu.executemany(insert_query, tuple)
        conn.commit()
        