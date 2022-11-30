from repositories.reference_repository import ReferenceRepository
from reference import Reference


class ReferenceService:
    """Class resposible for the application logic. """

    def __init__(self):
        self._reference_repository = ReferenceRepository()

    def add_reference(self, reference):
        """Adds one reference to the reference repository. """
        self._reference_repository.add(Reference(
            reference["authors"], reference["title"], reference["publisher"], reference["year"]))

    def get_references(self):
        """Translates the reference object to more human-readable form to show for the user.

        Returns:
            list: Returns complete strings of references as a list
        """
        references = []
        for reference in self._reference_repository.find_all():
            reference = reference.data
            authors = ""
            splitted_authors = reference["authors"].split(' and ')
            for author in splitted_authors:
                if author == splitted_authors[-1] and len(splitted_authors) > 1:
                    authors += " and "
                elif author != splitted_authors[0]:
                    authors += ", "
                if ", " in author:
                    names = author.split(", ")
                    authors += names[1] + " " + names[0]
                else:
                    authors += author
            references.append(
                authors + ". " + reference["title"] + ". " + reference["publisher"] + ", "
                + reference["year"] + ".")
        return references
