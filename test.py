from lib.sqlite_io import create_connection, run_sql_query, get_columns_list

from config import DB_NAME

conn = create_connection(DB_NAME)

print("Check project table content")
sql_select_projects = "SELECT * FROM projects;"
print(run_sql_query(conn, sql_select_projects))

print("Check tasks table content")
sql_select_tasks_of_project = "SELECT * FROM tasks WHERE project_id = 2;"
print(run_sql_query(conn, sql_select_tasks_of_project))

print("Check tasks table columns")
print(get_columns_list(conn, "tasks"))
