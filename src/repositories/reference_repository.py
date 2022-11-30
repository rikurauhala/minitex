class ReferenceRepository:
    """Saves the references to a list."""

    def __init__(self):
        """Initializes the list."""
        self.references = []

    def add(self, reference):
        """Adds one reference to the list."""
        self.references.append(reference)

    def find_all(self):
        """Finds all references in the repository.

        Returns:
            list: Returns all of the references as a list
        """
        return self.references
