from repositories.database import Repository
from entities.reference import Reference


class ReferenceService:
    """Class responsible for the application logic. """

    def __init__(self):
        """Initializes a new ReferenceService."""
        self._reference_repository = Repository()

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
            referenceobject = Reference(
                reference[1],
                reference[2],
                str(reference[3]),
                reference[4]
            )
            references.append(referenceobject)
        return references
