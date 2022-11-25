class Reference:
	def __init__(self, author: str, title: str, year: str, publisher: str) -> None:
		self._author = author
		self._title = title
		self._year = year
		self._publisher = publisher

		self._key = self.gen_key()


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
	def data(self):
		return 

	def gen_key(self):
		raise NotImplementedError

	