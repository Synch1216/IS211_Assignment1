#part 2
class Book:
	def __init__ (self, author='',title=''):
		self.author = author
		self.title = title
		def display(self):
			print "%s, written by %s" (self.author, self.title)

			one= Book('John Steinbeck', 'Of Mice and Men')
			two= Book('Harper Lee', 'To Kill A Mockingbird')
			one.display()
			two.display()