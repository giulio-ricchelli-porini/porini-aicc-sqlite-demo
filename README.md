# SQLite Demo

This project represents an example of usage of the [sqlite](https://www.sqlite.org/index.html) Python library.

## Assignment steps
* As done in the first assignment, clone this repo in the "GitClass" folder ("C:\Users\\%yourUsername%\Visual Studio Code\GitClass"); you should then have a new project folder in the "GitClass" folder dedicated to this project
* Check the projects files: the "main.py" file creates DBs and tables and populates them; the "test.py" file can be used to check the DBs' and tables' main features
* Update the code:
    * Update the "tasks" table so that it can also contain the name of the person to whom the task has been assigned (as a string), in a new attribute called "assigned_to"
    * Update the ".gitignore" file so that Git ignores all the files with the ".db" extension in the project root folder, not only the one currently configured: to test this you can change the DB_NAME value in the "config.py" file, re-generate DBs and tables, and check that the db file is not included in the Git changes from the integrated "Source Control" tab in VSCode (check the documentation to understand how to ignore files with a given extension)
* By using the integrated "Source Control" tab in VSCode, write a commit message and commit your changes
* Push your changes to the "main" branch through the same tab (through the "Sync Changes" button)
* From the browser, open the repository and check that your changes are now registered on the remote repository: you made your commits available to your (hypothetical) collaborators!

You completed the assignment! Please notify us when you have done!
