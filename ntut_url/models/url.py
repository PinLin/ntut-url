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
            name TEXT,
            target TEXT,
            PRIMARY KEY (name)
            )''')

    @staticmethod
    def create(name: str, target: str):
        db = sqlite3.connect(db_file)
        cursor = db.cursor()
        cursor.execute('''INSERT INTO url VALUES (?, ?)''', [name, target])
        db.commit()

    @staticmethod
    def is_exist(name: str):
        db = sqlite3.connect(db_file)
        cursor = db.cursor()
        cursor.execute('SELECT COUNT(*) FROM url WHERE name = ?', [name])

        return cursor.fetchone()[0] != 0

    @classmethod
    def find_all(clas):
        db = sqlite3.connect(db_file)
        cursor = db.cursor()
        cursor.execute('SELECT name FROM url')

        result = []
        for name, in cursor.fetchall():
            result.append(clas(name))

        return result

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
