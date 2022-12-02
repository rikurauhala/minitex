import sqlite3

class Repository:
    
    def __init__(self):
        self.connection = sqlite3.connect("references.db")
        self.cursor = self.connection.cursor()
        try:
            self.create_table()
        except:
            pass

    def create_table(self):
        self.cursor.execute("CREATE TABLE bookreferences (id INTEGER PRIMARY KEY, author TEXT, title TEXT, year INTEGER, publisher TEXT);")

    def add(self, reference):
        authors, title, year, publisher = reference.author, reference.title, reference.year, reference.publisher
        self.cursor.execute("INSERT INTO bookreferences (author, title, year, publisher) VALUES (?, ?, ?, ?)", (authors, title, int(year), publisher))
        self.connection.commit()
        
    def find_all(self):
        references = self.cursor.execute("SELECT * FROM bookreferences")
        return references
