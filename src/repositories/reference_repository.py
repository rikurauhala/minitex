from database import get_database_connection


class ReferenceRepository:
    def __init__(self, connection):
        self._connection = connection
        self._cursor = self._connection.cursor()

    def create(self, reference):
        authors = reference.author
        title = reference.title
        year = reference.year
        publisher = reference.publisher
        self._cursor.execute(
            "INSERT INTO bookreferences (author, title, year, publisher) VALUES (?, ?, ?, ?)",
            (authors, title, int(year), publisher)
        )
        self._connection.commit()

    def find_all(self):
        references = self._cursor.execute("SELECT * FROM bookreferences")
        return references


reference_repository = ReferenceRepository(get_database_connection())
