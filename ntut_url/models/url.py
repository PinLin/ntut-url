import sys
import sqlite3

db_file = sys.path[0] + '/ntut_url/db/ntut_url.db'


class Url:
    def __init__(self, name: str):
        self.__db = sqlite3.connect(db_file)

        self.__name = name

    @staticmethod
    def create_table():
        db = sqlite3.connect(db_file)
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS url (
            _id INTEGER,
            name TEXT,
            target TEXT,
            PRIMARY KEY (_id)
            )''')

    @staticmethod
    def create(name: str, target: str):
        db = sqlite3.connect(db_file)
        cursor = db.cursor()
        cursor.execute('''INSERT INTO url
            (name, target) VALUES (?, ?)''', [name, target])
        db.commit()

    @staticmethod
    def check_name(name: str):
        db = sqlite3.connect(db_file)
        cursor = db.cursor()
        cursor.execute('SELECT COUNT(*) FROM url WHERE name = ?', [name])

        return cursor.fetchone()[0] != 0

    @property
    def name(self):
        cursor = self.__db.cursor()
        cursor.execute('SELECT name FROM url WHERE name = ?',
                       [self.__name])

        return cursor.fetchone()[0]

    @property
    def target(self):
        cursor = self.__db.cursor()
        cursor.execute('SELECT target FROM url WHERE name = ?',
                       [self.__name])

        return cursor.fetchone()[0]
