import re

class Reference:
	def __init__(self, author: str, title: str, year: str, publisher: str) -> None:
		self._author = author
		self._title = title
		self._year = year
		self._publisher = publisher
		self._key = self._gen_key()

	@property
	def author(self):
		return self._author
	
	@property
	def title(self):
		return self._title
	
	@property
	def year(self):
		return self._year

	@property
	def publisher(self):
		return self._publisher

	@property
	def data(self) -> dict:
		"""Generates data form the refence object that can be then used
		to handle objects fields.

		Returns:
			dict: Reference object data as dict
		"""
		reference = {
			"key": self._key,
			"authors": self._author,
			"title": self._title,
			"year": self._year,
			"publisher": self._publisher
		}
		return reference

	def _gen_key(self) -> str:
		"""Generates key attribute for reference based on the authors lastnames
		and the publishing year

		Returns:
			str: generated key for the reference object
		"""
		authors = re.split(' and ', self._author)
		names_splitted = [lname.split(" ") for lname in authors]
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
			key = ""

			for name in last_names:
				key += name[0]

		key += self.year[-2:]

		return key