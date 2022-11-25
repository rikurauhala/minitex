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

	def _gen_key(self):
		return


if __name__ == "__main__":
	author = "Allan Collins and John Seely Brown and Ann Holum"
	title = "Cognitive apprenticeship: making thinking visible"
	journal = "American Educator"
	year = "1991"
	r = Reference(author, title, journal, year)
	
	print(r.author)
	print(r.title)
	print(r.publisher)
	print(r.year)

	print(r.data)