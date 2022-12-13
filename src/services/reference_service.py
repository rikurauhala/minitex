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

    def get_reference(self, index):
        """Fetches one reference from the list.

        Returns:
            reference: Returns a reference object.
        """
        references = self._references
        if len(references) > index >= 0:
            return self._references[index]
        return False

    def get_references(self):
        """Fetches a list of references in a readable form.

        Returns:
            list: Returns a list of references as strings.
        """
        return self._references

    def _import_all_references_to_memory(self):
        """Imports all references from database to a list kept in ReferenceService."""
        for reference in self._reference_repository.find_all():
            reference_object = Reference(
                reference[1],
                reference[2],
                str(reference[3]),
                reference[4]
            )
            self._references.append(reference_object)

    def delete_reference(self, reference):
        """Deletes a reference.

        Args:
            reference (Reference): A reference to be deleted.
        """
        self._reference_repository.delete(reference)
        self._references = []
        self._import_all_references_to_memory()

    def delete_all(self):
        """Deletes all references."""
        self._reference_repository.delete_all()
        self._references = []

    def edit_reference(self, new_value, index, column):
        """Edits a reference.

        Args:
            new_value (string): New value to replace the old.
            index (integer): Index of the reference to be edited.
            column (integer): 1: author, 2: title, 3: year, 4: publisher.
        """
        self._reference_repository.edit(new_value, index, column)
        self._references = []
        self._import_all_references_to_memory()
