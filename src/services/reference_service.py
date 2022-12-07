from entities.reference import Reference

from repositories.reference_repository import reference_repository


class ReferenceService:
    """Class responsible for the application logic."""

    def __init__(self):
        """Initializes a new ReferenceService."""
        self._reference_repository = reference_repository
        self._references = []
        self._import_all_references_to_memory()

    def add_reference(self, reference):
        """Adds one reference to the reference repository."""
        new_reference = Reference(
            reference["authors"],
            reference["title"],
            reference["year"],
            reference["publisher"]
        )
        self._reference_repository.create(new_reference)
        self._references.append(new_reference)

    def get_references(self):
        """Fetches a list of references in a readable form.

        Returns:
            list: Returns a list of references as strings.
        """
        return self._references

    def _import_all_references_to_memory(self):
        """Imports all references from database to a list kept in ReferenceService
        """
        for reference in self._reference_repository.find_all():
            reference_object = Reference(
                reference[1],
                reference[2],
                str(reference[3]),
                reference[4]
            )
            self._references.append(reference_object)

    def delete_reference(self, reference):
        self._reference_repository.delete(reference)
