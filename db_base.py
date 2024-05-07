import sqlite3

class DBbase:

    _conn = None
    _cursor = None

    def __init__(self, db_name):
        self._db_name = db_name
        self.connect()

    def connect(self):
        # create a connection to the database and cursor object
        self._conn = sqlite3.connect(self._db_name)
        self._cursor = self._conn.cursor()

    def execute_script(self, sql_string):
        # execute a script on the database
        self._cursor.executescript(sql_string)

    @property
    def get_cursor(self):
        # return the cursor object
        return  self._cursor

    @property
    def get_connection(self):
        # return the database connection object
        return self._conn

    def close_db(self):
        # close the database connection
        self._conn.close()
