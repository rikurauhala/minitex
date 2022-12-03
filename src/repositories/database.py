import sqlite3


class Repository:
    def __init__(self):
        self.connection = sqlite3.connect("references.db")
        self.cursor = self.connection.cursor()
        try:
            self.create_table()
        except sqlite3.OperationalError:
            pass

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE bookreferences (
                id INTEGER PRIMARY KEY,
                author TEXT,
                title TEXT,
                year INTEGER,
                publisher TEXT
            )"""
        )
    
    def drop_tables(self):
        self.cursor.execute("""
            DROP TABLE IF EXISTS bookreferences;
        """)
        self.connection.commit()

    def add(self, reference):
        authors = reference.author
        title = reference.title
        year = reference.year
        publisher = reference.publisher
        self.cursor.execute(
            "INSERT INTO bookreferences (author, title, year, publisher) VALUES (?, ?, ?, ?)",
            (authors, title, int(year), publisher)
        )
        self.connection.commit()

    def find_all(self):
        references = self.cursor.execute("SELECT * FROM bookreferences")
        return references
