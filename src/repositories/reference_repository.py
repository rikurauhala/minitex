from database import get_database_connection


class ReferenceRepository:
    def __init__(self, connection):
        """Initializes a new reference repository.

        Args:
            connection (Connection): Connection to the database.
        """
        self._connection = connection
        self._cursor = self._connection.cursor()

        self._querybuilds = {
            1: "author = ? WHERE ID = ?",
            2: "title = ? WHERE ID = ?",
            3: "year = ? WHERE ID = ?",
            4: "publisher = ? WHERE ID = ?"
        }

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

    def edit(self, new_value, index, column):
        """Edits a reference in the database.

        Args:
            new_value (string): New value to replace the old.
            index (integer): Index of the reference to be edited.
            column (integer): 1: author, 2: title, 3: year, 4: publisher.
        """
        query = "UPDATE bookreferences set " + self._querybuilds[column]
        self._cursor.execute(
            query, (new_value, index)
        )
        self._connection.commit()

    def delete(self, reference):
        """Deletes a reference from the database.

        Args:
            reference (Reference): The reference to be deleted.
        """
        self._cursor.execute(
            "DELETE FROM bookreferences WHERE author=? AND title=? AND year=? AND publisher=?",
            (reference.author, reference.title, reference.year, reference.publisher))
        self._connection.commit()

    def delete_all(self):
        """Deletes all references from the database."""
        self._cursor.execute("DELETE FROM bookreferences")
        self._connection.commit()


reference_repository = ReferenceRepository(get_database_connection())
