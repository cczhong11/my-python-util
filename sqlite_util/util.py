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

def insert_database(filename, insert_query, tuple_data):
    with sqlite3.connect(filename) as conn:
        cu = conn.cursor()
        if tuple_data.__class__.__name__ == "list":
            cu.executemany(insert_query, tuple_data)
        else:
            cu.execute(insert_query, tuple_data)
        conn.commit()
        
def update_database(filename, update_query, dict_data):
    with sqlite3.connect(filename) as conn:
        cu = conn.cursor()
        cu.execute(update_query,dict_data)
        conn.commit() 