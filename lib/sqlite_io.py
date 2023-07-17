import sqlite3


def create_connection(db_file):
    return sqlite3.connect(db_file)


def run_sql_query(connection, query):
    cursor = connection.cursor()
    res = cursor.execute(query)
    connection.commit()
    return res.fetchall()


def get_columns_list(connection, table_name):
    cursor = connection.cursor()
    res = cursor.execute(f"SELECT * FROM {table_name}")
    return [description[0] for description in res.description]
