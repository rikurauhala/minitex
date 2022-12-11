from database import get_database_connection


class ReferenceRepository:
    def __init__(self, connection):
        """Initializes a new reference repository.

        Args:
            connection (Connection): Connection to the database.
        """
        self._connection = connection
        self._cursor = self._connection.cursor()

    def create(self, reference):
        """Creates a new reference in the database.

        Args:
            reference (Reference): A reference object.
        """
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
        """Finds all reference objects in the database.

        Returns:
            references: All references in the database.
        """
        references = self._cursor.execute("SELECT * FROM bookreferences")
        return references

    def delete(self, reference):
        self._cursor.execute(
            "DELETE FROM bookreferences WHERE author=? AND title=?  AND year=? AND publisher=?",
            (reference.author, reference.title, reference.year, reference.publisher))
        self._connection.commit()

    def edit(self, value, indx, column):
        query = "UPDATE bookreferences set "
        if column == 1:
            query += "author = ? WHERE ID = ?"
        elif column == 2:
            query += "title = ? WHERE ID = ?"
        elif column == 3:
            query += "year = ? WHERE ID = ?"
        else:
            query += "publisher = ? WHERE ID = ?"
        self._cursor.execute(
            query, (value, indx)
        )
        self._connection.commit()


reference_repository = ReferenceRepository(get_database_connection())
