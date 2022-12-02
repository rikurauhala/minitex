import sqlite3

class Repository:
    
    def __init__(self):
        self.connection = sqlite3.connect("references.db")
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("CREATE TABLE references (id INTEGER PRIMARY KEY, author TEXT, title TEXT, year INTEGER, publisher TEXT);")

    def add(self, authors, title, year, publisher):
        self.cursor.execute("INSERT INTO references (author, title, year, publisher) VALUES (?, ?, ?, ?)", (authors, title, int(year), publisher))

    def find_all(self):
        references = self.cursor.execute("SELECT * FROM references")
        return references