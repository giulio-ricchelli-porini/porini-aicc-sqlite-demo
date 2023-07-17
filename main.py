from config import DB_NAME

from lib.sqlite_io import create_connection, run_sql_query
from lib.queries import SQL_CREATE_PROJECTS_TABLE, SQL_CREATE_TASKS_TABLE, SQL_INSERT_PROJECTS, SQL_INSERT_TASKS

print("Creating DB and tables")
conn = create_connection(DB_NAME)
run_sql_query(conn, SQL_CREATE_PROJECTS_TABLE)
run_sql_query(conn, SQL_CREATE_TASKS_TABLE)
print("DB and tables created successfully")

print("Inserting data in tables")
run_sql_query(conn, SQL_INSERT_PROJECTS)
run_sql_query(conn, SQL_INSERT_TASKS)
print("Data inserted successfully")
