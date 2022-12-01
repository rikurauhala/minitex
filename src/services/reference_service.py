from repositories.reference_repository import ReferenceRepository
from entities.reference import Reference


class ReferenceService:
    """Class responsible for the application logic. """

    def __init__(self):
        """Initializes a new ReferenceService."""
        self._reference_repository = ReferenceRepository()

    def add_reference(self, reference):
        """Adds one reference to the reference repository. """
        new_reference = Reference(
            reference["authors"],
            reference["title"],
            reference["year"],
            reference["publisher"]
        )
        self._reference_repository.add(new_reference)

    def get_references(self):
        """Fetches a list of references in a readable form.

        Returns:
            list: Returns a list of references as strings.
        """
        references = []
        for reference in self._reference_repository.find_all():
            references.append(reference)
        return references
