import re

from utils import validators


class Reference:
    """Object representing a reference."""

    def __init__(self, author: str, title: str, year: str, publisher: str) -> None:
        """Initializes a new Reference.

        Args:
            author (str): Author of the reference.
            title (str): Title of the reference.
            year (str): Year published.
            publisher (str): Publisher of the reference.
        """
        self.author = author
        self.title = title
        self.year = year
        self.publisher = publisher

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, name: str) -> None:
        if validators.validate_attribute_string(name, "author"):
            self._author = name

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, name: str) -> None:
        if validators.validate_attribute_string(name, "title"):
            self._title = name

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: str) -> None:
        if validators.validate_attribute_string(value, "year"):
            self._year = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, name: str) -> None:
        if validators.validate_attribute_string(name, "publisher"):
            self._publisher = name

    @property
    def data(self) -> dict:
        """Generates data form the refence object that can be then used
        to handle objects fields.

        Returns:
            dict: Reference object data as dict
        """
        return {"key": self._gen_key(), "authors": self._author, "title": self._title,
                "year": self._year, "publisher": self._publisher}

    def _gen_key(self) -> str:
        """Generates key attribute for reference based on the authors lastnames
        and the publishing year

        Returns:
            str: generated key for the reference object
        """
        authors = re.split(" and ", self._author)
        names_splitted = [last_name.split(" ") for last_name in authors]
        last_names = []

        for name in names_splitted:
            try:
                if "," in name[0]:
                    last_names.append(name[0].strip(","))
                else:
                    last_names.append(name[-1])
            except IndexError:
                last_names.append(name[0].strip(","))

        if len(last_names) == 1:
            key = last_names[0]
        else:
            key = "".join(name[0] for name in last_names)
        key += self.year[-2:]

        return key

    def __str__(self):
        """Returns the data of the reference in a readable form.

        Returns:
            string (str): A string representation of the Reference object.
        """
        authors = ""
        splitted_authors = self.author.split(" and ")
        for author in splitted_authors:
            if author == splitted_authors[-1] and len(splitted_authors) > 1:
                authors += " and "
            elif author != splitted_authors[0]:
                authors += ", "
            if ", " in author:
                names = author.split(", ")
                first_name = names[1]
                last_name = names[0]
                authors += f"{first_name} {last_name}"
            else:
                authors += author
        return f"{authors} | {self.title} | {self.publisher} ({self.year})"
