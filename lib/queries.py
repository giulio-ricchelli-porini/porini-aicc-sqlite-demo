SQL_CREATE_PROJECTS_TABLE = """
    CREATE TABLE IF NOT EXISTS projects (
        id integer PRIMARY KEY,
        name text NOT NULL,
        begin_date text,
        end_date text);
"""
SQL_CREATE_TASKS_TABLE = """
    CREATE TABLE IF NOT EXISTS tasks (
        id integer PRIMARY KEY,
        name text NOT NULL,
        priority integer,
        status_id integer NOT NULL,
        project_id integer NOT NULL,
        begin_date text NOT NULL,
        end_date text NOT NULL,
        FOREIGN KEY (project_id) REFERENCES projects (id));
"""

SQL_INSERT_PROJECTS = """
    INSERT INTO projects (id, name, begin_date, end_date)
        VALUES
            (1, 'Boring migration project', '2023-07-01', '2024-01-31'),
            (2, 'Phantasmagorical AI project', '2023-11-01', '2024-07-31');
"""
SQL_INSERT_TASKS = """
    INSERT INTO tasks (id, name, priority, status_id, project_id, begin_date, end_date)
        VALUES
            (1, 'Collect requirements', 5, 0, 1, '2023-07-01', '2023-10-01'),
            (2, 'Check integrations', 4, 0, 1, '2023-10-01', '2023-12-01'),
            (3, 'Implement pipelines', 3, 0, 1, '2023-12-01', '2024-03-01'),
            (4, 'Deploy and test', 2, 0, 1, '2024-03-01', '2024-07-31'),
            (5, 'Labelling', 5, 0, 2, '2023-11-01', '2024-01-01'),
            (6, 'Training', 4, 0, 2, '2024-01-01', '2024-03-01'),
            (7, 'Testing', 3, 0, 2, '2023-03-01', '2023-06-01'),
            (8, 'Deploy', 2, 0, 2, '2023-06-01', '2024-07-31');
"""
